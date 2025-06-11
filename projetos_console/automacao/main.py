import pyautogui as auto

def limpar_credenciais():
    auto.write("git config --global --unset user.name")
    auto.press("enter")
    auto.write("git config --global --unset user.email")
    auto.press("enter")

if __name__ == "__main__":
    auto.PAUSE = 0.5

    msg_commit = input("Informe a mensegem do commit: ")

    limpar_credenciais()

    auto.write('git config --global user,name "M4uroM4rcos"')
    auto.press("enter")
    auto.write('git config --global user.email "mauro.marcos20@hotmail.com"')
    auto.press("enter")
    auto.write('git add .')
    auto.press("enter")
    auto.write(f'git commit -m "{msg_commit}"')
    auto.press("enter")
    auto.write("git push")
    auto.press("enter")

    limpar_credenciais()