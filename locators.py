from selenium.webdriver.common.by import By

#Страница "Восстановить пароль"
class ForgotPasswordLocators:

    #поле "Email"
    #EMAIL_FIELD = By.XPATH, "(//div[contains(.,'Email')])[5]"
    EMAIL_FIELD = By.CSS_SELECTOR, ".input"

    #Поле Email в активном состоянии
    EMAIL_FIELD_ACTIVE = By.XPATH, "//input[@class='text input__textfield text_type_main-default']"

    #Кнопка "Восстановить"
    RESET_PASSWORD_BUTTON = By.XPATH, "//button[contains(.,'Восстановить')]"

    #Надпись "Вспомнили пароль?"
    REMEMBER_PASSWORD_BUTTON = By.XPATH, "//p[contains(.,'Вспомнили пароль? Войти')]"

#Страница восстановления пароля с полем для ввода нового
class ResetPasswordLocators:

    #Поле "Пароль"
    NEW_PASSWORD_FIELD = By.XPATH, "//label[contains(.,'Пароль')]"

    #Иконка видимости пароля в виде глаза - открытый глаз, пароль закрыт точками
    VIEW_PASSWORD_BUTTON = By.XPATH, '//div[@class="input__icon input__icon-action"]'

    #Поле ввода кода из письма
    EMAIL_CODE_FIELD = By.XPATH, "//label[contains(.,'Введите код из письма')]"

    #Поле "Пароль" с типом изменившимся на text
    PASSWORD_FIELD2 = By.XPATH, "//input[contains(@type,'text')]"


#Страница логина
class LoginPageLocators:

    #Кнопка "Восстановить пароль"
    FORGOT_PASSWORD_BUTTON = By.XPATH, "//a[contains(.,'Восстановить пароль')]"

    #Поле "Email" в неактивном состоянии
    EMAIL_FIELD_INACTIVE = By.XPATH, "(//div[contains(.,'Email')])[5]"

    #Поле Email в активном состоянии
    EMAIL_FIELD_ACTIVE = By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]"

    #Поле "Пароль" в неактивном состоянии
    PASSWORD_FIELD_INACTIVE = By.XPATH, "//label[contains(.,'Пароль')]"

    #Поле "Пароль" в активном состоянии
    PASSWORD_FIELD_ACTIVE = By.XPATH, "//input[contains(@name,'Пароль')]"

    #Кнопка "Войти"
    LOGIN_BUTTON = By.XPATH, "//button[contains(.,'Войти')]"

#Главная страница
class MainPageLocators:

    #Кнопка "Личный кабинет"
    GO_TO_PROFILE_BUTTON = By.XPATH, "//p[contains(.,'Личный Кабинет')]"

    #Кнопка "Лента заказов"
    GO_TO_ORDER_FEED_BUTTON = By.XPATH, "//p[contains(.,'Лента Заказов')]"

    #Кнопка "Оформить заказ"
    ORDER_BUTTON = By.XPATH, "//button[contains(.,'Оформить заказ')]"

    #Ингредиент Флюоресцентная булка
    FLUO_BUN = By.XPATH, "(//p[contains(.,'Флюоресцентная булка R2-D3')])"

    #Место для перетаскивания ингредиента
    INGREDIENT_PLACE = By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']"

    #Каунтер Флюоресцентной булки
    FLUO_BUN_COUNTER = By.XPATH, "//p[@class='counter_counter__num__3nue1' and text()='2']"

#Личный кабинет
class ProfileLocators:

    #Кнопка в хедере для перехода в раздел "История заказов"
    ORDER_HISTORY_BUTTON = By.XPATH, "//a[contains(.,'История заказов')]"

    #Кнопка "Выход"
    LOGOUT_BUTTON = By.XPATH, "//button[@type='button'][contains(.,'Выход')]"

    #Надпись о ПД
    PERSONAL_DATA_INFORMER = By.XPATH, "//p[contains(.,'персональные данные')]"

#Страница ленты заказов
class OrderFeedLocators:

    #Кнопка в хедере для перехода в раздел "Конструктор"
    GO_TO_CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(.,'Конструктор')]"

    #Заголовок страницы
    FEED_HEADER = By.XPATH, "//h1[contains(.,'Лента заказов')]"

    #Первый зааказ в списке
    FIRST_ORDER = By.XPATH, "(//h2[contains(@class,'main-medium mb-2')])[1]"

    #Конкретный заказ
    SPECIFIC_ORDER_LOCATOR = By.XPATH, "//p[@class='text text_type_digits-default'][contains(.,'#{}')]"

    #Общее количество заказов
    TOTAL = By.XPATH, "(// p[contains( @class ,'digits-large')])[1]"

    #Количество заказов за текущий день
    TODAYS_TOTAL = By.XPATH, "(//p[contains(@class,'digits-large')])[2]"

#Попап заказа в Ленте
class OrderPopupFeedLocators:

    #Заголовок "Состав" в попапе
    CONTENTS_HEADER = By.XPATH, "//p[contains(.,'Cостав')]"

#Попап с деталями ингредиента
class IngredientPopupLocators:

    #Заголовок попапа
    INGREDIENT_HEADER = By.XPATH, "//h2[contains(.,'Детали ингредиента')]"

    #Иконка "Крестик"
    POPUP_CLOSE_BUTTON = By.XPATH, "(//button[contains(@type,'button')])[1]"


#Попап с номером заказа
class OrderCreatedLocators:

    #Текст в попапе
    POPUP_TEXT = By.XPATH, "//p[contains(.,'идентификатор заказа')]"

    #Кнопка Крестик
    CLOSE_BUTTON = By.XPATH, "//button[contains(@type,'button')]"

    #Неправильный номер
    INCORRECT_NUMBER = By.XPATH, "//h2[contains(.,'9999')]"

    #Номер только что созданного заказа
    JUST_CREATED_ORDER = By.XPATH, "//h2[contains(@class,'digits-large mb-8')]"

    #Локатор для ожидания
    WAITING_FOR = By.XPATH, "//li[@class='text text_type_digits-default mb-2'][contains(.,'{}')]"

#История заказов в профиле
class OrderHistoryLocators:

    #Номер заказа пользователя
    ORDER_NUMBER = By.XPATH, "//p[@class='text text_type_digits-default'][contains(.,'#')]"






