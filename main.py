import streamlit as st
import numpy as np
from  PIL import Image
import streamlit.components.v1 as components
import cv2

st.set_page_config(
    page_title="XAIFEATURES",
    page_icon="",
)

def format_dropdown_labels(val):
    return METHODS[val]['name']

def home():
    #logo = Image.open(r"./assets/images/logo_ufsj_01.jpg")
    #profile = Image.open(r"./assets/images/logo_dcomp_ufsj.png")

    #col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    #with col1:
    #    st.image(logo, width = 250, use_column_width = False)
    #with col3: 
    #    st.image(profile, width = 200)

    st.write(
        "<h1 style='text-align: justify;'>Automatic features extraction from the optic cup and disc segmentation for Glaucoma classification</h1>",  unsafe_allow_html=True
    )    
    
    #st.sidebar.info("Bem-vindo(a) ao XAIGLAUCOMA")

    st.markdown(
        """
        <div style='text-align: justify;'>
        O glaucoma é uma doença que afeta progressivamente o nervo óptico, principal causa de cegueira no mundo.
        Uma das estratégias mais assertivas para fazer o diagnóstico é a Tomografia de Coerência Óptica (OCT) que identifica
        Anomalias na anatomia do nervo óptico. A OCT é um exame de alto custo, por isso alguns trabalhos na literatura vêm utilizando
        redes neurais profundas, computacionalmente caras, para realizar análises em imagens de fundo de retina para di diagnosticar glaucoma. 
        Como alternativa a essas abordagens, neste trabalho propomos um método computacional de baixo custo para extrair características da anatomia 
        do nervo óptico (ou seja, escavação óptica e segmentação do disco) por meio do processamento de imagens de fundo de retina, que são usadas em 
        conjunto com algoritmos de classificação de custo computacional mais baixo (ou seja, SVM), são capazes de realizar diagnósticos precisos. 
        Mais especificamente, quanto mais precisa a extração de recursos, maior a precisão do classificador.
        
        
        </div>
        """, unsafe_allow_html=True
    )

def upload_neural_network():
    
    import os.path
    import pathlib
    
    
    #st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')

    st.write(
        """
        Faça o upload do arquivo CSV.
        
        Obs.: Somente arquivos .csv são permitidos. 
        """)
    
    st.sidebar.info("Área destinada ao upload de rede neural treinada.")

    uploaded_file = st.file_uploader("Selecione o arquivo", type=["csv"], accept_multiple_files = False)

    if uploaded_file is not None:
        file_details = {"filename":uploaded_file.name, "filetype":uploaded_file.type, "filesize":uploaded_file.size}
        st.write(file_details)
        #st.image(Image.open(uploaded_file), width=250)
    
    def upload():
        if uploaded_file is None:
            st.session_state["upload_state"] = "Atenção! Carregue um arquivo primeiro."
        else:
            #data = uploaded_file.getvalue().decode('utf-8')
            parent_path = pathlib.Path(__file__).parent.parent.resolve()           
            save_path = os.path.join(parent_path, "xaiglaucoma/assets/models")
            complete_name = os.path.join(save_path, uploaded_file.name)
            destination_file = open(complete_name, "wb")
            with destination_file as f:
                f.write((uploaded_file).getbuffer())
                f.close()
                st.session_state["upload_state"] = "Arquivo salvo com sucesso!"
                st.success('Arquivo salvo com sucesso!', icon="✅")
                #st.session_state["upload_state"] = "O arquivo foi salvo com sucesso!" + complete_name + " successfully!"

    st.button("Enviar", on_click=upload)
    


def app():
    
    #logo = Image.open(r"./assets/images/logo_ufsj_01.jpg")
    #profile = Image.open(r"./assets/images/logo_dcomp_ufsj.png")

    #col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    #with col1:
    #    st.image(logo, width = 250, use_column_width = False)
    #with col3: 
    #    st.image(profile, width = 200)

    #st.markdown(f'# Módulo {list(page_names_to_funcs.keys())[1]}')

    st.write(
        """
        Faça o upload da imagem de fundo de olho (retinografia) a ser analisada pela aplicação.
        
        Atenção! A imagem deve estar com a área de interesse (disco óptico) recortada.

        Obs.: Formatos de arquivos aceitos: JPG, JPEG e PNG. 
        """)
    
    uploaded_file = st.file_uploader("Selecione a imagem", type = ["jpg","jpeg", "png"], accept_multiple_files = False)

    if uploaded_file is not None:

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        import roi

        rSize = 400
        #rW,rw,rH,rh,fw,fh,nerve,fnW,fnH,img = roi.isolaNervo(image,rSize)
        gray, minVal, maxVal, minLoc, maxLoc, isolated_nerve = roi.isolaNervo(image, rSize)

        #st.image(isolated_nerve)
        #st.write(isolated_nerve.shape, isolated_nerve.dtype)

        import equalization

        img_eq = equalization.equalization(isolated_nerve)
        #st.image(img_eq)
        #st.write(img_eq.shape, img_eq.dtype)

        import segmentation

        #disc, rect_disc = segmentation.segmentation_disc(isolated_nerve, img_eq)
        #st.image(disc)
        #st.image(rect_disc)
        
        rect_disc,Xrec_disc,xrec_disc,Yrec_disc,yrec_disc = segmentation.segmentation_disc(isolated_nerve, img_eq)
        st.image(rect_disc) 
        st.write("Delimitação das extremidades do Disco Óptico")

        rect_cup,Xrec_cup,xrec_cup,Yrec_cup,yrec_cup = segmentation.segmentation_cup(isolated_nerve, img_eq)
        st.image(rect_cup) 
        st.write("Delimitação das extremidades da Copa Óptica")


def applyShap(image):
    
    import shap_xai
    shap_xai.shap(image)


page_names_to_funcs = {
    "Início": home,
    "Aplicação": app
}

demo_name = st.sidebar.selectbox("Selecione uma opção no menu abaixo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()    
