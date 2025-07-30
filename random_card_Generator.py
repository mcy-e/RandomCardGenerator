from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
    
Config.set('graphics', 'borderless', '0')
Config.set('graphics', 'shadow', '0')
#? didn't have time to write comments i was on rush
#* had to switch to md no classics
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem
from kivy.uix.button import Button
from kivy.metrics import dp,sp
from kivy.graphics import Line, Color,Rectangle
from kivy.clock import Clock
from kivy.properties import BooleanProperty,StringProperty,ObjectProperty
from kivy.factory import Factory
from functools import partial
from kivy.utils import platform
#*some use modules
import random
import json
import os
#* global var but i recommend not using it
auto_dismiss=1/60
sixtyFPS=1/60
#* class init
class WindowManager(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class ShuffleScreen(Screen):
    pass

class Pool_popup_WindowManager(ScreenManager):
    pass

class Pool_name_screen(Screen):
    pass

class Pool_list_screen(Screen):
    pass

class pool_creation_content(MDBoxLayout):
    pass

class item_edit_content(MDBoxLayout):
    pass

class cards_content(MDBoxLayout):
    pass

#* classes with working logic
class MainScreenWidget(MDFloatLayout):
    nothing_label=StringProperty('NO POOL')
    editing_button = ObjectProperty(None)
    delete_mode = BooleanProperty(False)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class pool_creation_popup(MDDialog):
    opened_by_plus = BooleanProperty(True) 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not hasattr(self, 'content_cls') or self.content_cls is None:
            self.content_cls = pool_creation_content()
        self.list_of_items = list(reversed(self.content_cls.ids.l_widget.ids.list_items.children))
        self.backup_list = self.content_cls.ids.l_widget.ids.list_items.children
        self.backup_items = []  
        self.backup_name = ""   
        self.content_cls.ids.save_btn.bind(on_release=self.save_list)
        self.content_cls.ids.close_btn.bind(on_release=self.cancel)
        
        if sixtyFPS > 0:
            Clock.schedule_interval(self.enable_saving, sixtyFPS)
        else:
            Clock.schedule_interval(self.enable_saving, 1/60)  

    def enable_saving(self, dt):
        try:
            self.list_of_items = list(reversed(self.content_cls.ids.l_widget.ids.list_items.children))
            if len(self.list_of_items) <= 1:
                self.content_cls.ids.save_btn.disabled = True
            else:
                self.content_cls.ids.save_btn.disabled = False
        except (AttributeError, KeyError) as e:
            print(f"Error in init widgets {e}")
            
   
    def save_list(self, *args):
        try:
            pool = App.get_running_app().root.ids.main_sec.ids.main_widget.ids.main_widget_pools
            name_of_list = self.content_cls.ids.ln_widget
            self.list_of_items = list(reversed(self.content_cls.ids.l_widget.ids.list_items.children))
            
            text_name = name_of_list.ids.name_entered.text.strip()
            if text_name and len(self.list_of_items) > 1:
                if self.opened_by_plus:
                
                    max_chars_pool = 10  
                    display_name = text_name if len(text_name) <= max_chars_pool else text_name[:max_chars_pool] + "..."
                    Color_list=[
                        (0.36, 0.42, 0.75, 0.5),  
                        (0.49, 0.34, 0.76, 0.5),  
                        (0.15, 0.65, 0.60, 0.5),  
                        (0.0, 0.67, 0.76, 0.5),   
                        (1.0, 0.70, 0.0, 0.5),     
                        (1.0, 0.65, 0.15, 0.5),     
                        (0.49, 0.70, 0.26, 0.5),   
                    ]
                    b = MDRaisedButton(
                        text=display_name,
                        size_hint=(0.5, 1),
                        md_bg_color=random.choice(Color_list),
                        elevation=2,
                        padding=(10, 10),
                        font_size='16sp',
                    )
                  
                    b.full_pool_name = text_name
                    main_screen = MDApp.get_running_app().root.ids.main_sec.ids.main_widget
                    b.items = self.list_of_items
                
                    b.bind(on_press=lambda instance: self.pool_button_pressed(instance, main_screen))
                    pool.add_widget(b)
                else:
                    if self.editing_button:
                      
                        max_chars_pool = 10
                        display_name = text_name if len(text_name) <= max_chars_pool else text_name[:max_chars_pool] + "..."
                        self.editing_button.text = display_name
                        self.editing_button.full_pool_name = text_name
                        self.editing_button.items = self.list_of_items

                Clock.schedule_once(self.dismiss, auto_dismiss)
        except (AttributeError, KeyError) as e:
            print(f"Error in save_list: {e}")   
    
    def pool_button_pressed(self, btn_instance, main_screen):
        try:
            main_screen = App.get_running_app().root.ids.main_sec.ids.main_widget
            if main_screen.delete_mode:
                parent = btn_instance.parent
                if parent:
                    parent.remove_widget(btn_instance)
            else:
                self.open_to_edit(btn_instance)        
        except (AttributeError, KeyError) as e:
            print(f"Error in pool_button_pressed: {e}")
            
    def cancel(self, *args):
        if not self.opened_by_plus and self.editing_button:
            if hasattr(self, 'backup_name'):
                
                max_chars_pool = 10
                display_name = self.backup_name if len(self.backup_name) <= max_chars_pool else self.backup_name[:max_chars_pool] + "..."
                self.editing_button.text = display_name
                self.editing_button.full_pool_name = self.backup_name
            
            if hasattr(self, 'backup_items'):
                self.editing_button.items = self.backup_items
        elif self.opened_by_plus:
            container = self.content_cls.ids.l_widget.ids.list_items
            container.clear_widgets()
            self.content_cls.ids.ln_widget.ids.name_entered.text = ""
            
        self.dismiss()       
    
    def open_to_edit(self, instance_btn):
        try:
            self.opened_by_plus = False
            self.editing_button = instance_btn 
            old_transition = self.content_cls.ids.wind_manager.transition
            self.content_cls.ids.wind_manager.transition = NoTransition()  
            self.content_cls.ids.wind_manager.current = "list_name"
            self.content_cls.ids.wind_manager.transition = old_transition  
            self.open()
            

            original_pool_name = getattr(instance_btn, 'full_pool_name', instance_btn.text)
            self.content_cls.ids.ln_widget.ids.name_entered.text = original_pool_name
            
            original_text = original_pool_name  
            self.backup_name = original_text
            
            container = self.content_cls.ids.l_widget.ids.list_items
            container.clear_widgets()
            self.backup_items = []  
            
            if hasattr(instance_btn, 'items') and instance_btn.items:
                for item in instance_btn.items:
                    
                    full_text = getattr(item, 'full_text', item.text)
                    backup_btn = Button(text=full_text, size_hint=(None, None), size=(dp(80), dp(30)))
                    backup_btn.font_size = sp(backup_btn.height * 0.5)
                    backup_btn.full_text = full_text  
                    self.backup_items.append(backup_btn)
                    

                    max_chars = 12
                    display_text = full_text if len(full_text) <= max_chars else full_text[:max_chars] + "..."
                    
                    new_btn = MDRaisedButton(
                        text=display_text,
                        size_hint=(1, None),
                        height=dp(40),
                        md_bg_color=(0.3, 0.3, 0.4, 0.7),
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1)
                    )
                    new_btn.full_text = full_text  
                    new_btn.text_size = (dp(95), None)
                    new_btn.bind(on_release=self.content_cls.ids.l_widget.show_options)
                    container.add_widget(new_btn)
            
            original_list = list(reversed(container.children))
            self.change_event = None  
            
            def trigger_changes(self, txt_ori, lst_ori):
                try:
                    changed_text = False
                    current_list = list(reversed(self.content_cls.ids.l_widget.ids.list_items.children))
                    
                    if len(lst_ori) == len(current_list):
                        for i, current_btn in enumerate(current_list):
                            if i < len(self.backup_items):
                               
                                current_full_text = getattr(current_btn, 'full_text', current_btn.text)
                                backup_full_text = getattr(self.backup_items[i], 'full_text', self.backup_items[i].text)
                                if current_full_text != backup_full_text:
                                    changed_text = True
                                    break
                            else:
                                changed_text = True
                                break
                    else:
                        changed_text = True  
                    
                    current_name = self.content_cls.ids.ln_widget.ids.name_entered.text
                    current_list_len = len(current_list)
                    
                    if changed_text:
                        self.list_of_items = current_list
                        self.content_cls.ids.save_btn.disabled = False
                        instance_btn.items = self.list_of_items
                        
                    if (txt_ori != current_name and current_list_len > 1):
                        self.content_cls.ids.save_btn.disabled = False
                        self.list_of_items = current_list
                        instance_btn.items = self.list_of_items
                        
                    if (len(self.backup_items) != current_list_len and current_list_len > 1):
                        self.content_cls.ids.save_btn.disabled = False
                        self.list_of_items = current_list
                        instance_btn.items = self.list_of_items
                    
                    if (not changed_text and txt_ori == current_name and len(self.backup_items) == current_list_len):
                        self.content_cls.ids.save_btn.disabled = True
                            
                    if (len(lst_ori) > current_list_len or changed_text) and hasattr(self.content_cls.ids, 'close_btn') and self.content_cls.ids.close_btn.state == 'down':
                        container = self.content_cls.ids.l_widget.ids.list_items
                        container.clear_widgets()
                        
                        self.content_cls.ids.ln_widget.ids.name_entered.text = self.backup_name
                        
                        for widget in self.backup_items:
                            full_text = getattr(widget, 'full_text', widget.text)
                            max_chars = 12
                            display_text = full_text if len(full_text) <= max_chars else full_text[:max_chars] + "..."
                            
                            new_widget = MDRaisedButton(
                                text=display_text,
                                size_hint=(None, None),
                                size=(dp(100), dp(40)),
                                md_bg_color=(0.2, 0.2, 0.2, 1),
                                theme_text_color="Custom",
                                text_color=(1, 1, 1, 1)
                            )
                            new_widget.full_text = full_text
                            new_widget.text_size = (dp(95), None)
                            new_widget.bind(on_release=self.content_cls.ids.l_widget.show_options)
                            container.add_widget(new_widget)
                        
                        if self.change_event:
                            self.change_event.cancel()
                        self.dismiss()
                        
                except (AttributeError, KeyError) as e:
                    print(f"Error in trigger_changes: {e}")
                    return False  
            
            self.change_event = Clock.schedule_interval(lambda dt: trigger_changes(self, original_text, original_list), sixtyFPS)
            
        except (AttributeError, KeyError) as e:
            print(f"Error in open_to_edit: {e}")

class Name_list_widget(MDFloatLayout):
    enter_pressed = BooleanProperty(False)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        if sixtyFPS > 0:
            Clock.schedule_interval(self.Auto_check,sixtyFPS)
        else:
            Clock.schedule_interval(self.Auto_check, 1/60)
        
    def Auto_check(self,dt):
        try:
            user_input = self.ids.name_entered.text.strip()
            if user_input == "":
                self.enter_pressed = False
                
            else:
                self.enter_pressed = True
        except (AttributeError, KeyError):
            self.enter_pressed = False
        
    def show_validation(self):
        try:
            user_input = self.ids.name_entered.text.strip()
            if user_input == "":
                self.enter_pressed = False
            else:
                self.enter_pressed = True
        except (AttributeError, KeyError):
            self.enter_pressed = False

class List_widget(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_item(self):
        try:
            input_string = self.ids.list_entered.text.strip()
            if input_string:
                
                max_chars = 12  
                display_text = input_string if len(input_string) <= max_chars else input_string[:max_chars] + "..."
                
                b = MDRaisedButton(
                    text=display_text,
                    size_hint=(1, None),
                    height=dp(40),
                    md_bg_color=(0.3, 0.3, 0.4, 0.7),
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),
                    halign="center",
                    valign="center",
                )
               
                b.full_text = input_string
                b.text_size = (dp(95), None)  
                b.bind(on_release=self.show_options)
                self.ids.list_items.add_widget(b)
                self.ids.list_entered.text = ""

                Clock.schedule_once(lambda dt: setattr(self.ids.list_entered, 'focus', True), 0.1)
        except Exception as e:
            print(f"Error adding item: {e}")
            
    def show_options(self, instance_btn):
        try:
            content = item_edit_content()
            item = item_of_list(content_cls=content)
            
            original_text = getattr(instance_btn, 'full_text', instance_btn.text)
            content.ids.item_name.text = original_text
            
            def edit_item(*args):
                try:
                    item_text = content.ids.item_name.text.strip()
                    if item_text:
                        
                        max_chars = 12
                        display_text = item_text if len(item_text) <= max_chars else item_text[:max_chars] + "..."
                        instance_btn.text = display_text
                        instance_btn.full_text = item_text
                        content.ids.label_text.text = 'Item Name has Been Edited'
                        Clock.schedule_once(item.dismiss, 1/4)
                    else:
                        content.ids.label_text.text = 'Error Empty Name'
                except (AttributeError, KeyError) as e:
                    print(f"Error in edit_item: {e}")
                    
            def remove_item(*args):
                try:
                    content.ids.item_name.text = ''
                    content.ids.label_text.text = 'Item Removed!'
                    if instance_btn.parent:  
                        self.ids.list_items.remove_widget(instance_btn)
                    Clock.schedule_once(item.dismiss, 1/2)
                except (AttributeError, KeyError) as e:
                    print(f"Error in remove_item: {e}")
                    
            content.ids.edit_btn.bind(on_press=edit_item)
            content.ids.remove_btn.bind(on_press=remove_item)
            item.title = f'Edit Item List' 
            item.open()      
        except (AttributeError, KeyError) as e:
            print(f"Error in show_options: {e}")

class item_of_list(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CardsPopUp(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ShuffleScreenWidget(MDFloatLayout):
    result = ObjectProperty([])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        if not self.result:
            self.result = []
        self.selected_pool = ""
        self.menu_items = []
        self.dropdown_menu = None
        self.get_names_event = Clock.schedule_interval(lambda dt: self.get_names(dt, self.result), sixtyFPS)
        
    def open_pool_menu(self):
        try:
            menu_items = []
            for name, _ in self.result:
                menu_items.append({
                    "text": name,
                    "viewclass": "OneLineListItem", 
                    "height": dp(48),
                    "on_release": lambda x=name: self.menu_callback(x),
                })
            
            self.dropdown_menu = MDDropdownMenu(
                caller=self.ids.select_pool_button,
                items=menu_items,
                width_mult=5,
                max_height=dp(300),  
                border_margin=dp(8),  
                ver_growth="down",
                position="bottom",
            )
            self.dropdown_menu.open()
        except Exception as e:
            print(f"Error in open_pool_menu: {e}")
    
    def menu_callback(self, pool_name):
        try:
            self.selected_pool = pool_name
            self.ids.select_pool_button.text = pool_name
            self.ids.label_text.text = f"'{pool_name}' POOL IS SELECTED"
            if self.dropdown_menu:
                self.dropdown_menu.dismiss()
        except Exception as e:
            print(f"Error in menu_callback: {e}")
    
    def get_names(self, dt, _):
        try:
            pool = App.get_running_app().root.ids.main_sec.ids.main_widget.ids.main_widget_pools
            self.result.clear()

            for btn in pool.children:
                if isinstance(btn, (Button, MDRaisedButton)):

                    pool_name = getattr(btn, 'full_pool_name', btn.text)
                    item_list = getattr(btn, 'items', [])

                    item_list_string = [getattr(b, 'full_text', b.text) for b in item_list if hasattr(b, 'text')] if item_list else []
                    self.result.append((pool_name, item_list_string))

        except (AttributeError, KeyError) as e:
            print(f"Error in get_names: {e}")

    def empty_label(self, dt):
        try:
            self.ids.label_text.text = ''
        except (AttributeError, KeyError):
            pass
            
    def randomize(self):
        try:
            selected_value = self.selected_pool

            if not selected_value or selected_value == "Select Pool":
                self.ids.label_text.text = 'NO POOL IS SELECTED'
                Clock.schedule_once(self.empty_label, 1)
                return

            if self.get_names_event:
                self.get_names_event.cancel()
                self.get_names_event = None

            item_list = None
            for name, lst in self.result:
                if name == selected_value:
                    item_list = lst
                    break

            if item_list and len(item_list) > 0:
                temp_list = item_list[:]
                chosen_elem = random.choice(temp_list)
                temp_list.remove(chosen_elem)

                content = cards_content()
                cards_pp = CardsPopUp(content_cls=content)
                content.ids.label_text.text = chosen_elem

                content.ids.next.bind(on_release=lambda instance: self.show_next(cards_pp, temp_list, content))

                cards_pp.open()
            else:
                self.ids.label_text.text = 'POOL IS EMPTY'
                Clock.schedule_once(self.empty_label, 1)

            if not self.get_names_event:
                self.get_names_event = Clock.schedule_interval(lambda dt: self.get_names(dt, self.result), sixtyFPS)
                
        except (AttributeError, KeyError, IndexError) as e:
            print(f"Error in randomize: {e}")
            try:
                self.ids.label_text.text = 'ERROR OCCURRED'
                Clock.schedule_once(self.empty_label, 2)
            except:
                pass
                
    def show_next(self, popup_instance, item_l, content):
        try:
            if item_l:
                chosen_elem = random.choice(item_l)
                item_l.remove(chosen_elem)
                content.ids.label_text.text = chosen_elem
            else:
                Clock.schedule_once(lambda dt: popup_instance.dismiss(), 1/60)
        except (AttributeError, KeyError, IndexError) as e:
            print(f"Error in show_next: {e}")
            try:
                content.ids.label_text.text = 'ERROR OCCURRED'
                Clock.schedule_once(lambda dt: popup_instance.dismiss(), 1/10)
            except:
                pass


class Application(MDApp):

    def get_app_path(self):
        try:
            return os.path.join(self.user_data_dir, 'POOLS.json')
        except Exception as e:
            print(f"Error getting app path: {e}")
            return 'POOLS.json'  
            
    def on_start(self):
        self.theme_cls.theme_style = "Dark" 
        self.theme_cls.primary_palette = "Indigo"    
        self.theme_cls.accent_palette = "Amber"  
        self.theme_cls.radius = 'Medium'
        self.theme_cls.card_radius = [15, 15, 15, 15]
        self.theme_cls.button_radius = [10, 10, 10, 10]
        self.theme_cls.primary_hue = "600"           
        self.theme_cls.accent_hue = "500"
        try:
            data = self.load_POOLS()
            pool = self.root.ids.main_sec.ids.main_widget.ids.main_widget_pools
            main_screen = self.root.ids.main_sec.ids.main_widget
            pop_up = pool_creation_popup(content_cls=pool_creation_content())
            
            for entry in data:
                if not isinstance(entry, dict) or 'text' not in entry or 'items' not in entry:
                    print(f"Skipping invalid entry: {entry}")
                    continue
                

                pool_name = entry['text']
                max_chars_pool = 10
                display_pool_name = pool_name if len(pool_name) <= max_chars_pool else pool_name[:max_chars_pool] + "..."
                Color_list=[
                    (0.36, 0.42, 0.75, 0.5),  
                    (0.49, 0.34, 0.76, 0.5),  
                    (0.15, 0.65, 0.60, 0.5),  
                    (0.0, 0.67, 0.76, 0.5),   
                    (1.0, 0.70, 0.0, 0.5),     
                    (1.0, 0.65, 0.15, 0.5),     
                    (0.49, 0.70, 0.26, 0.5),   
                ]
                b = MDRaisedButton(
                    text=display_pool_name,
                    size_hint=(0.5, 1),
                    md_bg_color=random.choice(Color_list),
                    elevation=2,
                    padding=(10, 10),
                    font_size='16sp',
                )
                
                b.full_pool_name = pool_name
                
                restored_items = []
                
                if isinstance(entry['items'], list) and entry['items']:
                    for txt in entry['items']:
                        if isinstance(txt, str) and txt.strip():
                            
                            max_chars = 12
                            display_text = txt if len(txt) <= max_chars else txt[:max_chars] + "..."
                            
                            item_btn = MDRaisedButton(
                                text=display_text,
                                size_hint=(1, None),    
                                height=dp(40),                                
                                md_bg_color=(0.3, 0.3, 0.4, 0.7),  
                                theme_text_color="Custom",
                                text_color=(1, 1, 1, 1),
                                halign="center",  
                                valign="center",  
                            )
                            item_btn.text_size = (dp(95), None)
                            item_btn.full_text = txt  
                            

                            item_btn.bind(on_release=pop_up.content_cls.ids.l_widget.show_options)
                            
                            restored_items.append(item_btn)
                            
                b.items = restored_items
                b.bind(on_press=lambda instance: pop_up.pool_button_pressed(instance, main_screen))
                pool.add_widget(b)
                
        except (AttributeError, KeyError) as e:
            print(f"Error in on_start: {e}")
    
    def on_stop(self):
        try:
            pool = self.root.ids.main_sec.ids.main_widget.ids.main_widget_pools
            data = []
            
            for btn in reversed(pool.children):
                if isinstance(btn, MDRaisedButton):
                    items = getattr(btn, 'items', [])
                    
                    
                    pool_name = getattr(btn, 'full_pool_name', btn.text)
                    
                    item_texts = []
                    if items:
                        for item in items:
                            if hasattr(item, 'full_text'):
                                
                                if item.full_text.strip():
                                    item_texts.append(item.full_text)
                            elif hasattr(item, 'text') and item.text.strip():
                                item_texts.append(item.text)
                    
                    pool_data = {'text': pool_name, 'items': item_texts}
                    data.append(pool_data)
                    
            self.save_POOLS(data)
            
        except (AttributeError, KeyError) as e:
            print(f"Error in on_stop: {e}")

    def save_POOLS(self, btn_data):
        try:
            path = self.get_app_path()
            dir_path = os.path.dirname(path)
            if dir_path:  
                os.makedirs(dir_path, exist_ok=True)
            
            with open(path, 'w') as file:
                json.dump(btn_data, file, indent=2)
           
        except (IOError, OSError) as e:
            print(f"Error saving POOLS: {e}")

    def load_POOLS(self):
        try:
            path = self.get_app_path()
            print(f"Loading from: {path}")
            if os.path.exists(path):
                with open(path, 'r') as f:
                    data = json.load(f)
                    
                    if isinstance(data, list):
                        return data
                    else:
                        print("Invalid data format in POOLS.json")
                        return []
            else:
                print("POOLS.json file doesn't exist")
        except (json.JSONDecodeError, IOError, OSError) as e:
            print(f"Error loading POOLS: {e}")
        return []
    
if __name__=='__main__':
    Application().run()