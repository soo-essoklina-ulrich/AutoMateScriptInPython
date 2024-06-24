import pyautogui
import time


# Fonction pour cliquer à une position spécifique plusieurs fois
def click_button(x, y, clicks, interval):
    for _ in range(clicks):
        pyautogui.click(x, y)
        time.sleep(interval)


def determiner_position_en_cours():
    print('Position de la souris :', pyautogui.position())
    return pyautogui.position()


def clickinposictionactuel(click, interval):
    for _ in range(click):
        pyautogui.click(determiner_position_en_cours())
        time.sleep(interval)




# Position du bouton sur l'écran de l'ordinateur
button_x = 1640  # Remplacez par la position x du bouton
button_y = 575  # Remplacez par la position y du bouton

# Nombre de clics et intervalle entre les clics en secondes
num_clicks = 3010
# convert num_click to int
num_clicks = int(num_clicks)

click_interval = 0.01

# Appel de la fonction pour cliquer
# click_button(button_x, button_y, num_clicks, click_interval)
clickinposictionactuel(num_clicks, click_interval)
