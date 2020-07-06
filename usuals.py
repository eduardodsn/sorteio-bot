import time
import random
from selenium import webdriver
from tkinter import scrolledtext
from selenium.webdriver.common.keys import Keys


class UsualFunctions:
    def __init__(self, user, password, link, quantity):
        from dashboard import Dashboard
        self.driver = webdriver.Chrome()
        self.target_accounts = ['jairmessiasbolsonaro', 'raulgil3', 'neymarjr',
                                'realdonaldtrump', 'gabigol', 'cristiano',
                                'fatimabernardes', 'anapaulapadraooficial', 'rodrigomaiarj',
                                'astarforbants', 'mosalah', 'arianagrande',
                                'flamengo', 'liverpoolfc', 'fcbarcelona',
                                'spacex', 'leomessi', 'brunomars']
        self.user = user
        self.password = password
        self.sorteio_link = link
        self.quantity_to_tag = int(quantity)
        self.scapegoats = []
        self.define_dashboard(Dashboard)
    

    def define_dashboard(self, Dashboard):
        self.dashboard = Dashboard
        self.log = self.dashboard.create_log_screen(self)
        self.box = self.dashboard.create_log_scrolled_text(self, self.log)
        self.print_log('Iniciando bot...')
        
    
    # adiciona nova mensagem ao log do tkinter
    def print_log(self, message):
        self.dashboard.generate_log(self, self.log, self.box, message)


    # sorteia as contas do self.target_accounts para extrair bodes expiatorios
    def draw_target_accounts(self):
        self.shuffle_list(self.target_accounts)
        self.selected_target_accounts = []
        self.unselected_target_accounts = self.target_accounts

        # quantidade de contas alvo para extrair (10 contas)
        for i in range (0, 18):
            while True:
                position = random.randint(0, 17)
                try:
                    self.selected_target_accounts.append(self.unselected_target_accounts[position])
                    del self.unselected_target_accounts[position]
                except:
                    pass
                else:
                    break


    # exporta seguidores das contas alvo selecionadas e embaralha a lista
    def export_followers(self):
        for selected_target_account in self.selected_target_accounts:
            self.access_zasasa(selected_target_account)
            self.click_input_export()
            self.click_submit()
            self.get_scapegoats()
            self.sleep(2)
        self.shuffle_list(self.scapegoats)
        self.print_log(f'Total de bodes expiatórios: {len(self.scapegoats)}')


    # adiciona a lista de bodes expiatorios as contas extraidas
    def get_scapegoats(self):
        self.print_log('Extraindo bodes expiatórios...')

        #quantide de bodes expiatorios para extrair (100 contas)
        for i in range (2, 101):
            self.scapegoats.append(self.driver.find_element_by_xpath(f'//*[@id="div_data"]/table/tbody/tr[{i}]/td[1]').text)


    # entra no site zasasa para extrair bodes expiatorios
    def access_zasasa(self, selected_target_account):
        self.driver.get('http://zasasa.com/en/export_instagram_followers_list.php')
        urlInput = self.driver.find_element_by_xpath('//*[@id="url"]')
        urlInput.click
        urlInput.send_keys(selected_target_account)
        self.print_log(f'Conta selecionada: {selected_target_account}')


    # clica no botao enviar no site zasasa
    def click_submit(self):
        submitButton = self.driver.find_element_by_xpath('/html/body/center/form/input[7]')
        submitButton.click()


    # clica no input para digitar conta no site zasasa
    def click_input_export(self):
        input_export = self.driver.find_element_by_xpath('/html/body/center/form/input[3]')
        input_export.click()


    # embaralha listas
    def shuffle_list(self, lista):
        lista = random.sample(lista, len(lista))


    # loga no Instagram
    def login(self):
        self.print_log('Logando no Instagram...')
        try:
            self.driver.get('https://www.instagram.com/accounts/login/')
            self.sleep(2)
            self.type_login()
            self.type_pass()
        except NameError:
            print(NameError)
        else:
            self.sleep(3)
            self.print_log('Logado!')
            self.go_to_draw_link()


    # digita login no Instagram
    def type_login(self):
        self.print_log('Inserindo login...')
        input_login = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        input_login.click()
        input_login.send_keys(self.user)


    # digita senha no Instagram
    def type_pass(self):
        self.print_log('Inserindo senha...')
        input_pass = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        input_pass.click()
        input_pass.send_keys(self.password) 
        input_pass.send_keys(Keys.ENTER)

    
    # entra no link do sorteio
    def go_to_draw_link(self):
        self.print_log('Entrando no link do sorteio...')
        self.driver.get(self.sorteio_link)


    # comenta as contas em self.scapegoats de acordo com self.quantity_to_tag
    def comment_scapegoats(self):
        self.print_log('Comentando...')

        i = 0
        while len(self.scapegoats) >= self.quantity_to_tag:
            self.tag_quantity_scapegoats()
            i += 1
            self.print_log(f'Total de comentários: {i}')
            

    # marca a quantidade definida pelo usuario e envia o comentario
    def tag_quantity_scapegoats(self):
        textarea = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea')
        textarea.click()
        textarea = self.driver.find_element_by_css_selector(".Ypffh.focus-visible")
        textarea.send_keys(self.tag_aux())
        self.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()
        self.sleep(0.5)



    # funcao auxiliar para gerar o comentario
    def tag_aux(self):
        comment = ''

        for i in range(1, self.quantity_to_tag+1):
            comment += f'@{self.scapegoats[0]} '
            del self.scapegoats[0]
        return comment


    # pausa
    def sleep(self, pause):
        time.sleep(pause)
        

# funcao para criar instanciar classe e iniciar o bot
def run_bot(user, password, link, quantity):
    bot = UsualFunctions(user, password, link, quantity)
    try:
        bot.driver.maximize_window()
        bot.draw_target_accounts()
        bot.export_followers()
        bot.login()
        bot.comment_scapegoats()
        bot.print_log('Comentários finalizados!')
    except:
        bot.print_log('Algo deu errado, finalizando bot!')
    finally:
        bot.print_log('Bot finalizado!')