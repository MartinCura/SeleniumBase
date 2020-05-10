# Dutch / Nederlands - Translations
from seleniumbase import BaseCase


class Testgeval(BaseCase):

    def url_openen(self, *args, **kwargs):
        # open(url)
        return self.open(*args, **kwargs)

    def klik(self, *args, **kwargs):
        # click(selector)
        return self.click(*args, **kwargs)

    def dubbelklik(self, *args, **kwargs):
        # double_click(selector)
        return self.double_click(*args, **kwargs)

    def klik_langzaam(self, *args, **kwargs):
        # slow_click(selector)
        return self.slow_click(*args, **kwargs)

    def klik_linktekst(self, *args, **kwargs):
        # click_link_text(link_text)
        return self.click_link_text(*args, **kwargs)

    def tekst_bijwerken(self, *args, **kwargs):
        # update_text(selector, new_value)
        return self.update_text(*args, **kwargs)

    def tekst_toevoegen(self, *args, **kwargs):
        # add_text(selector, new_value)
        return self.add_text(*args, **kwargs)

    def ontvang_tekst(self, *args, **kwargs):
        # get_text(selector, new_value)
        return self.get_text(*args, **kwargs)

    def controleren_tekst(self, *args, **kwargs):
        # assert_text(text, selector)
        return self.assert_text(*args, **kwargs)

    def controleren_exacte_tekst(self, *args, **kwargs):
        # assert_exact_text(text, selector)
        return self.assert_exact_text(*args, **kwargs)

    def controleren_linktekst(self, *args, **kwargs):
        # assert_link_text(link_text)
        return self.assert_link_text(*args, **kwargs)

    def controleren_element(self, *args, **kwargs):
        # assert_element(selector)
        return self.assert_element(*args, **kwargs)

    def controleren_titel(self, *args, **kwargs):
        # assert_title(title)
        return self.assert_title(*args, **kwargs)

    def controleren_ware(self, *args, **kwargs):
        # assert_true(expr)
        return self.assert_true(*args, **kwargs)

    def controleren_valse(self, *args, **kwargs):
        # assert_false(expr)
        return self.assert_false(*args, **kwargs)

    def controleren_gelijk(self, *args, **kwargs):
        # assert_equal(first, second)
        return self.assert_equal(*args, **kwargs)

    def controleren_niet_gelijk(self, *args, **kwargs):
        # assert_not_equal(first, second)
        return self.assert_not_equal(*args, **kwargs)

    def ververs_pagina(self, *args, **kwargs):
        # refresh_page()
        return self.refresh_page(*args, **kwargs)

    def huidige_url_ophalen(self, *args, **kwargs):
        # get_current_url()
        return self.get_current_url(*args, **kwargs)

    def broncode_ophalen(self, *args, **kwargs):
        # get_page_source()
        return self.get_page_source(*args, **kwargs)

    def terug(self, *args, **kwargs):
        # go_back()
        return self.go_back(*args, **kwargs)

    def vooruit(self, *args, **kwargs):
        # go_forward()
        return self.go_forward(*args, **kwargs)

    def tekst_zichtbaar(self, *args, **kwargs):
        # is_text_visible(text, selector="html")
        return self.is_text_visible(*args, **kwargs)

    def element_zichtbaar(self, *args, **kwargs):
        # is_element_visible(selector)
        return self.is_element_visible(*args, **kwargs)

    def element_aanwezig(self, *args, **kwargs):
        # is_element_present(selector)
        return self.is_element_present(*args, **kwargs)

    def wacht_op_tekst(self, *args, **kwargs):
        # wait_for_text(text, selector)
        return self.wait_for_text(*args, **kwargs)

    def wacht_op_element(self, *args, **kwargs):
        # wait_for_element(selector)
        return self.wait_for_element(*args, **kwargs)

    def wacht_op_element_aanwezig(self, *args, **kwargs):
        # wait_for_element_present(selector)
        return self.wait_for_element_present(*args, **kwargs)

    def slapen(self, *args, **kwargs):
        # sleep(seconds)
        return self.sleep(*args, **kwargs)

    def verzenden(self, *args, **kwargs):
        # submit(selector)
        return self.submit(*args, **kwargs)

    def js_klik(self, *args, **kwargs):
        # js_click(selector)
        return self.js_click(*args, **kwargs)

    def html_inspecteren(self, *args, **kwargs):
        # inspect_html()
        return self.inspect_html(*args, **kwargs)

    def bewaar_screenshot(self, *args, **kwargs):
        # save_screenshot(name)
        return self.save_screenshot(*args, **kwargs)

    def selecteer_bestand(self, *args, **kwargs):
        # choose_file(selector, file_path)
        return self.choose_file(*args, **kwargs)

    def voer_het_script_uit(self, *args, **kwargs):
        # execute_script(script)
        return self.execute_script(*args, **kwargs)

    def blokkeer_advertenties(self, *args, **kwargs):
        # ad_block()
        return self.ad_block(*args, **kwargs)

    def overslaan(self, *args, **kwargs):
        # skip(reason="")
        return self.skip(*args, **kwargs)

    def controleren_op_gebroken_links(self, *args, **kwargs):
        # assert_no_404_errors()
        return self.assert_no_404_errors(*args, **kwargs)

    def controleren_op_js_fouten(self, *args, **kwargs):
        # assert_no_js_errors()
        return self.assert_no_js_errors(*args, **kwargs)

    def overschakelen_naar_frame(self, *args, **kwargs):
        # switch_to_frame(frame)
        return self.switch_to_frame(*args, **kwargs)

    def overschakelen_naar_standaardcontent(self, *args, **kwargs):
        # switch_to_default_content()
        return self.switch_to_default_content(*args, **kwargs)

    def nieuw_venster_openen(self, *args, **kwargs):
        # open_new_window()
        return self.open_new_window(*args, **kwargs)

    def overschakelen_naar_venster(self, *args, **kwargs):
        # switch_to_window(window)
        return self.switch_to_window(*args, **kwargs)

    def overschakelen_naar_standaardvenster(self, *args, **kwargs):
        # switch_to_default_window()
        return self.switch_to_default_window(*args, **kwargs)

    def markeren(self, *args, **kwargs):
        # highlight(selector)
        return self.highlight(*args, **kwargs)

    def markeren_klik(self, *args, **kwargs):
        # highlight_click(selector)
        return self.highlight_click(*args, **kwargs)

    def scrollen_naar(self, *args, **kwargs):
        # scroll_to(selector)
        return self.scroll_to(*args, **kwargs)

    def naar_boven_scrollen(self, *args, **kwargs):
        # scroll_to_top()
        return self.scroll_to_top(*args, **kwargs)

    def naar_beneden_scrollen(self, *args, **kwargs):
        # scroll_to_bottom()
        return self.scroll_to_bottom(*args, **kwargs)

    def zweven_en_klik(self, *args, **kwargs):
        # hover_and_click(hover_selector, click_selector)
        return self.hover_and_click(*args, **kwargs)

    def is_het_geselecteerd(self, *args, **kwargs):
        # is_selected(selector)
        return self.is_selected(*args, **kwargs)

    def druk_op_pijl_omhoog(self, *args, **kwargs):
        # press_up_arrow(selector="html", times=1)
        return self.press_up_arrow(*args, **kwargs)

    def druk_op_pijl_omlaag(self, *args, **kwargs):
        # press_down_arrow(selector="html", times=1)
        return self.press_down_arrow(*args, **kwargs)

    def druk_op_pijl_links(self, *args, **kwargs):
        # press_left_arrow(selector="html", times=1)
        return self.press_left_arrow(*args, **kwargs)

    def druk_op_pijl_rechts(self, *args, **kwargs):
        # press_right_arrow(selector="html", times=1)
        return self.press_right_arrow(*args, **kwargs)

    def klik_zichtbare_elementen(self, *args, **kwargs):
        # click_visible_elements(selector)
        return self.click_visible_elements(*args, **kwargs)

    def optie_selecteren_per_tekst(self, *args, **kwargs):
        # select_option_by_text(dropdown_selector, option)
        return self.select_option_by_text(*args, **kwargs)

    def optie_selecteren_per_index(self, *args, **kwargs):
        # select_option_by_index(dropdown_selector, option)
        return self.select_option_by_index(*args, **kwargs)

    def optie_selecteren_per_waarde(self, *args, **kwargs):
        # select_option_by_value(dropdown_selector, option)
        return self.select_option_by_value(*args, **kwargs)

    def maak_een_tour(self, *args, **kwargs):
        # create_tour(name=None, theme=None)
        return self.create_tour(*args, **kwargs)

    def maak_een_shepherd_tour(self, *args, **kwargs):
        # create_shepherd_tour(name=None, theme=None)
        return self.create_shepherd_tour(*args, **kwargs)

    def maak_een_bootstrap_tour(self, *args, **kwargs):
        # create_bootstrap_tour(name=None, theme=None)
        return self.create_bootstrap_tour(*args, **kwargs)

    def maak_een_hopscotch_tour(self, *args, **kwargs):
        # create_hopscotch_tour(name=None, theme=None)
        return self.create_hopscotch_tour(*args, **kwargs)

    def maak_een_introjs_tour(self, *args, **kwargs):
        # create_introjs_tour(name=None, theme=None)
        return self.create_introjs_tour(*args, **kwargs)

    def toevoegen_tour_stap(self, *args, **kwargs):
        # add_tour_step(message, selector=None, name=None,
        #               title=None, theme=None, alignment=None)
        return self.add_tour_step(*args, **kwargs)

    def speel_de_tour(self, *args, **kwargs):
        # play_tour(name=None)
        return self.play_tour(*args, **kwargs)

    def de_tour_exporteren(self, *args, **kwargs):
        # export_tour(name=None, filename="my_tour.js", url=None)
        return self.export_tour(*args, **kwargs)

    def mislukken(self, *args, **kwargs):
        # fail(msg=None)  # Inherited from "unittest"
        return self.fail(*args, **kwargs)

    def url_ophalen(self, *args, **kwargs):
        # get(url)  # Same as open(url)
        return self.get(*args, **kwargs)

    def bezoek_url(self, *args, **kwargs):
        # visit(url)  # Same as open(url)
        return self.visit(*args, **kwargs)

    def element_ophalen(self, *args, **kwargs):
        # get_element(selector)  # Element can be hidden
        return self.get_element(*args, **kwargs)

    def vind_element(self, *args, **kwargs):
        # find_element(selector)  # Element must be visible
        return self.find_element(*args, **kwargs)

    def kenmerk_ophalen(self, *args, **kwargs):
        # get_attribute(selector, attribute)
        return self.get_attribute(*args, **kwargs)

    def kenmerk_instellen(self, *args, **kwargs):
        # set_attribute(selector, attribute, value)
        return self.set_attribute(*args, **kwargs)

    def kenmerken_instellen(self, *args, **kwargs):
        # set_attributes(selector, attribute, value)
        return self.set_attributes(*args, **kwargs)

    def voer(self, *args, **kwargs):
        # input(selector, new_value)  # Same as update_text()
        return self.type(*args, **kwargs)

    def schrijven(self, *args, **kwargs):
        # write(selector, new_value)  # Same as update_text()
        return self.write(*args, **kwargs)

    def afdrukken(self, *args, **kwargs):
        # print(TEXT)  # Same as Python print()
        return self.print(*args, **kwargs)
