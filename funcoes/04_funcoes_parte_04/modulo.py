# Importar biblioteca
import os

# Funções
def velocidade_media(vi, vf):
    vm = vf-vi
    return vm

def tempo_medio(tf, ti):
    tm = tf-ti
    return tm

def aceleracao_media(vm, tm):
    am = vm/tm
    return

def mru(si, v, t):
    s = si+v*t
    return s

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")