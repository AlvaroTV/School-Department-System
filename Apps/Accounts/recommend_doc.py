import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_absolute_error

def matrix_anteproyectos_materias(df_anteproyectos, df_anteproyecto_materia, df_materias):
    # Se eliminan aquellos atributos que no son necesarios y se renombra una columna para hacer la union con otro dataframe
    df_anteproyectos = df_anteproyectos.drop(['revisor1_id', 'revisor2_id', 'dependencia_id', 'asesorExterno_id', 'observacion_id', 'anteproyectoDoc', 'codigoUnion', 'fechaEntrega', 'numIntegrantes'], axis=1)
    df_anteproyectos.rename(columns = {'id':'anteproyecto_id'}, inplace = True)
    df_materias.rename(columns = {'id':'materia_id'}, inplace = True)
    
    # Union de anteproyecto con materia
    df_anteproyecto_materia_union = pd.merge(df_anteproyecto_materia, df_materias, on="materia_id")
    df_anteproyecto_materia_union = df_anteproyecto_materia_union.drop(['materia_id', 'nombre', 'semestre', 'id'], axis=1)
    
    # Se agrupan las materias por anteproyecto
    df_grouped = df_anteproyecto_materia_union.groupby(df_anteproyecto_materia_union.anteproyecto_id)
    
    # Se crea la matriz principal
    columns_series = df_materias['clave']
    columns_list = columns_series.tolist()
    columns_list.insert(0, 'anteproyecto_id')
    df_matrix_anteproyecto_materias = pd.DataFrame(columns=columns_list)
    
    # Se agrega cada anteproyecto con sus respectivas materias a la matriz
    for k, g in df_grouped:    
        list_keys = df_grouped.get_group(k)['clave']
        list_keys = list_keys.tolist()
        list_values = df_grouped.get_group(k)['compatibilidad']
        list_values = list_values.tolist()    
        dictionary_materias = {list_keys[i]: list_values[i] for i in range(len(list_keys))}    
        dictionary_materias['anteproyecto_id'] = k      
        df_dictionary = pd.DataFrame(dictionary_materias, index=[0])    
        df_matrix_anteproyecto_materias = df_matrix_anteproyecto_materias.append(df_dictionary, ignore_index = True)
    
    
    return df_matrix_anteproyecto_materias  

# Funcion que recibe un df de las materias, un df de los docentes y un df de 
# los perfiles academicos de cada docente
def matrix_docentes_materias(df_materias, df_docentes, df_perfil_academico):
    df_docentes = df_docentes[['id', 'perfilAcademico_id', 'nombre']]
    df_materias.rename(columns = {'id':'materia_id'}, inplace = True)
    columns_series = df_materias['clave']
    columns_list = columns_series.tolist()
    columns_list.insert(0, 'perfilAcademico_id')
    df_matrix_docentes_materias = pd.DataFrame(columns=columns_list)
    
    df_perfil_meteria_union = pd.merge(df_perfil_academico, df_materias, on="materia_id")
    df_perfil_meteria_union = df_perfil_meteria_union.drop(['materia_id'], axis=1)
    df_grouped = df_perfil_meteria_union.groupby(df_perfil_meteria_union.perfilacademico_id)
    
    for k, g in df_grouped:    
        list_keys = df_grouped.get_group(k)['clave']
        list_keys = list_keys.tolist()
        dictionary_keys = dict.fromkeys(list_keys, 10)    
        dictionary_keys['perfilAcademico_id'] = k  
        df_dictionary = pd.DataFrame(dictionary_keys, index=[0])
        df_matrix_docentes_materias = df_matrix_docentes_materias.append(df_dictionary, ignore_index = True)
    
    df_matrix_docentes_materias = pd.merge(df_docentes, df_matrix_docentes_materias, on='perfilAcademico_id')
    df_matrix_docentes_materias = df_matrix_docentes_materias.drop(['perfilAcademico_id'], axis=1)
    df_matrix_docentes_materias.rename(columns = {'id':'docente_id'}, inplace = True)
    
    return df_matrix_docentes_materias 

def recommend_docentes(anteproyectos_df, docentes_df, n):
    docentes_columns = docentes_df.columns.tolist()
    docentes_columns.pop(0)
    
    anteproyecto_pk = anteproyectos_df.iloc[0, 0]
    # Select user row from anteproyectos_df
    anteproyectos_scores = anteproyectos_df[anteproyectos_df['anteproyecto_id'] == anteproyecto_pk] 
    
    # Initialize empty match_scores column in docentes_df
    docentes_df['match_scores'] = 0
    
    # Iterate over each docente in docentes_df
    for i, docente in docentes_df.iterrows():
        # Initialize match_score for this docente
        match_score = 0
        
        # Iterate over each genre in docente
        for genre in docentes_columns:
            # If the user has a score for this genre and the docente has a score for this genre
            if not pd.isna(anteproyectos_scores[genre].values[0]) and not pd.isna(docente[genre]):
                # Calculate the absolute difference between the user's score and the docente's score
                match_score += abs(anteproyectos_scores[genre].values[0] - docente[genre])
                
        # Store match_score for thisdocente
        docentes_df.at[i, 'match_scores'] = match_score
    # sort docentes_df by match_scores in descending order
    docentes_df = docentes_df.sort_values(by='match_scores',ascending=False)
    # return the top n docentes
    top_docentes = docentes_df.head(n)
    # Convert a column of a Pandas dataframe to a list
    docentes_list = top_docentes['docente_id'].tolist()
    return docentes_list

def recomendaciones_docentes(df_anteproyectos, df_anteproyecto_materia, df_docentes, df_perfil_academico, df_materias, num_docentes = 3):
    mx_docentes = matrix_docentes_materias(df_materias, df_docentes, df_perfil_academico)
    mx_docentes = mx_docentes.drop('nombre', axis=1)
    mx_anteproyectos = matrix_anteproyectos_materias(df_anteproyectos, df_anteproyecto_materia, df_materias)
    
    docentes_columns = []
    anteproy_columns = []
    
    for i in range(1, 33):
        materia_str = 'materia_' + str(i)    
        docentes_columns.append(materia_str)
        anteproy_columns.append(materia_str)
    docentes_columns.insert(0, 'docente_id')
    anteproy_columns.insert(0, 'anteproyecto_id')
        
    for i, col in enumerate(mx_docentes.columns):    
        mx_docentes = mx_docentes.rename(columns={col: docentes_columns[i]})

    for i, col in enumerate(mx_anteproyectos.columns):    
        mx_anteproyectos = mx_anteproyectos.rename(columns={col: anteproy_columns[i]}) 
        
    anteproy_columns.pop(0)
    docentes_columns.pop(0)
        
    docentes_list = recommend_docentes(mx_anteproyectos, mx_docentes, num_docentes)
    return docentes_list
