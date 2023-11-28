from speech import indentify_speech as isp
from prompt import generate_response as gr
from speak import speak_text as st

def adele():
    x=isp()
    txt=gr(x)
    st(txt)
adele()