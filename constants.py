# Links for program to log-in and parse users
SITE_URL = "input your site URL here"
LOGIN_URL = SITE_URL + "/index.php?r=site%2Flogin"
USER_TABLE_URL = SITE_URL + "/index.php?r=clients%2Findex&page={}"

# Location of page elements which program interacts to
LOGIN_PATH = "/html/body/div[1]/div/div/section/div/form/div[1]/div[1]/input"
PASSWORD_PATH = "/html/body/div[1]/div/div/section/div/form/div[2]/div[1]/input"
BUTTON_PATH = "/html/body/div[1]/div/div/section/div/form/div[4]/div/button"
LAST_PAGE_PATH = "/html/body/div[1]/main/div/div/section/div/div/ul/li[11]/a"

# User credentials
LOGIN = "input your login here"
PASSWORD = "input your password here"
