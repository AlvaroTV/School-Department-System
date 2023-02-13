import pandas as pd
import numpy as np

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


def cosine_similarity(anteproyecto_scores, docente_scores):
    dot_product = np.dot(anteproyecto_scores, docente_scores)
    nrom_anteproyecto = np.linalg.norm(anteproyecto_scores)
    norm_docente = np.linalg.norm(docente_scores)
    return dot_product / (nrom_anteproyecto * norm_docente)

def recommend_docentes(anteproyectos_df, docentes_df, anteproyecto_id):
    # Select user row from anteproyectos_df
    anteproyecto_scores = anteproyectos_df[anteproyectos_df['anteproyecto_id'] == anteproyecto_id].drop(columns=['anteproyecto_id']).values[0]
    
    # Create a new dataframe to store the cosine similarity scores for each user-docente pair
    scores_df = pd.DataFrame(columns=['anteproyecto_id', 'docente_id', 'cosine_similarity_score'])
    
    # Iterate over each docente in docentes_df
    for i, docente in docentes_df.iterrows():
        # Get docente scores
        docente_scores = docente.drop(columns=['docente_id']).values
        
        # Calculate cosine similarity score between user scores and docente scores
        cosine_similarity_score = cosine_similarity(anteproyecto_scores, docente_scores)
        
        # Store cosine similarity score for this user-docente pair
        scores_df = scores_df.append({
            'anteproyecto_id': anteproyecto_id,
            'docente_id': docente['docente_id'],
            'cosine_similarity_score': cosine_similarity_score
        }, ignore_index=True)
        
    # sort scores_df by cosine_similarity_score in descending order
    scores_df = scores_df.sort_values(by='cosine_similarity_score',ascending=False)
    # return the top n docentes
    return scores_df.head(n=3)

