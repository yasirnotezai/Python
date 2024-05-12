'''

            ############## HOPE YOU LIKE IT ##############

'''


import tkinter as tk
from tkinter import ttk, Listbox, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import pandas as pd
import random


class PokemonGame:
    def __init__(self):
        self.selected_pokemon1 = None
        self.selected_pokemon2 = None
        # putting the values in the list
        self.battle_data = []

    def dataCleaning(self):   
        self.data = pd.read_csv("D:\\Coding\\PythonVScode\\PokemonProject\\pokemon.csv")
        self.copied_data = self.data.copy()
        self.copied_data = self.copied_data.drop(["Type 2", "Total", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"], axis=1)
        
        # dropping the duplicates 
        self.copied_data = self.copied_data.drop([19, 12, 7, 8, 3], axis=0)
        self.copied_data = self.copied_data.rename(columns={"Type 1": "Element"})
        
        # accessing the first 18 cleaned data as specified in the pdf
        self.copied_data = self.copied_data[:18]
        self.copied_data.to_csv("cleanPokeData.csv", index=False)

    def choose_pokemon_gui(self, score1=0, score2=0, health1=200, health2=200):
        def choose_pokemon_for_player(player):
            selected_pokemon = None  # Initialize selected pokemon variable

            def player_listbox_select(event=None):
                nonlocal selected_pokemon
                selected_pokemon = listBox.get(tk.ACTIVE)
                image_path = f"D:\\Coding\\PythonVScode\\PokemonProject\\Images\\{selected_pokemon}.png"
                image = Image.open(image_path)
                resized_image = image.resize((170, 170))
                image_reference = ImageTk.PhotoImage(resized_image)
                image_label.configure(image=image_reference)
                image_label.image = image_reference

            def choose_pokemon():
                nonlocal selected_pokemon
                selected_pokemon = listBox.get(tk.ACTIVE)
                root.quit()
                
            
            # Create a new Toplevel window
            root = tk.Toplevel()
            frame = tk.Frame(root)
            labelFrame = tk.LabelFrame(frame)
            labelFrame.grid(row=0, column=0)

            default_image_path = "D:\\Coding\\PythonVScode\\PokemonProject\\Images\\none.png"
            default_image = Image.open(default_image_path)
            default_resized_image = default_image.resize((170, 170))
            default_image = ImageTk.PhotoImage(default_resized_image)
            image_label = tk.Label(labelFrame, image=default_image)
            image_label.grid(row=1, column=1)

            label_text = f"Player {player} chooses Pokemon"
            label = tk.Label(labelFrame, font=('Times New Roman', 10, 'bold'), text=label_text)
            label.grid(row=0, column=0)

            warning_label = tk.Label(labelFrame, font=('Times New Roman', 9, 'bold'), text="Warning! Click the element in listBox \n two times for selection \n (Slowly).")
            warning_label.grid(row=2, column=0)

            listBox = Listbox(labelFrame, width=18, height=10)
            listBox.grid(row=1, column=0)
            pokemon_names = self.copied_data['Name'].tolist()
            for i in range(len(pokemon_names)):
                listBox.insert(i, pokemon_names[i])

            listBox.bind("<<ListboxSelect>>", player_listbox_select)

            button = ttk.Button(labelFrame, text="Choose!", command=choose_pokemon)
            button.grid(row=2, column=1, pady=10)

            frame.pack()
            root.mainloop()
            

            
            return selected_pokemon
        

       
       
        # Player 1 selects Pokemon
        self.selected_pokemon1 = choose_pokemon_for_player(1)

        # Player 2 selects Pokemon
        self.selected_pokemon2 = choose_pokemon_for_player(2)

        # Now, both players have selected their Pokemon, start the battle GUI
        battle_gui_instance = BattleGui(self, score1, score2, health1, health2)
        battle_gui_instance.gui3()
     
     
     # evolving and rechoosing           
    def evolve_pokemon(self, player):
        current_pokemon = self.selected_pokemon1 if player == 1 else self.selected_pokemon2
        selected_pokemon_row = self.copied_data[self.copied_data['Name'] == current_pokemon]
        evolved_pokemon = current_pokemon + "_evolved"  # Example: Pikachu_evolved
        if player == 1:
            self.selected_pokemon1 = evolved_pokemon
        else:
            self.selected_pokemon2 = evolved_pokemon
    
    
    # making the following columns heading in the excel file
    def collect_battle_data(self, pokemon1, pokemon2, damage1, damage2, health1 , health2, critical1, critical2 ,elemental1, elemental2):
        self.battle_data.append({
            'Pokemon 1': pokemon1,
            'Pokemon 2': pokemon2,
            'Damage 1': damage1,
            'Damage 2': damage2,
            'Health 1': health1,
            'Health 2': health2,
            'Critical 1': critical1,
            'Critical 2': critical2,
            'Elemental 1': elemental1,
            'Elemental 2': elemental2
        })
        
    # writing the pandas dataframe in the excel file
    def write_battle_data_to_excel(self):
        df = pd.DataFrame(self.battle_data)
        df.to_excel("battle_data.xlsx", index=False)

class BattleGui:
    def __init__(self, pokemon_game_instance, score1=0, score2=0, health1=200, health2=200):
        # initializing the neccessary variables 
        self.pokemon_game_instance = pokemon_game_instance
        self.image_references = []
        self.max_health1 = health1
        self.max_health2 = health2
        self.player1_score = score1
        self.player2_score = score2
        self.evolved_pokemon1 = None
        self.evolved_pokemon2 = None

    def gui3(self):
        
        # physical attack button modifications
        def attack_physical():
            new_health1 = 0
            new_health2 = 0
            nonlocal player_turn
            if player_turn == 1:
                
                self.opponent_health2 = progressbar2_1['value']
                selected_pokemon_row = self.pokemon_game_instance.copied_data[self.pokemon_game_instance.copied_data['Name'] == self.pokemon_game_instance.selected_pokemon1]
                
                # calculation for damage
                player_attack_value = selected_pokemon_row.iloc[0].get("Attack", 0)
                damageable_attack_value = int(random.randint(75, 100)  / 100 * float(player_attack_value))
                
                # calculation for health
                new_health1 = max(self.opponent_health2 - damageable_attack_value, 0)
                print(f"Player 2's {new_health1}")
                is_critical = 1 if new_health1 < 100 else 0
                is_elemental = False
                # collecting data and callimg making the excel file
                self.pokemon_game_instance.collect_battle_data(self.pokemon_game_instance.selected_pokemon1,
                                                               self.pokemon_game_instance.selected_pokemon2,
                                                               damageable_attack_value,
                                                               (damageable_attack_value * 0.8),
                                                               new_health1,
                                                               new_health2,
                                                               is_critical,
                                                               is_critical,
                                                               is_elemental,
                                                               is_critical)
                
                self.health_label2 = tk.Label(self.labelFrame, text=f"{new_health1}/{self.max_health1}",  font=('Times New Roman', 8, 'bold'))
                self.health_label2.grid(row=4, column=1)
                
                progressbar2_1['value'] = new_health1
                
                
                if new_health1 == 0:
                    self.max_health2 += 25
                    messagebox.showinfo("Result", "Player 1 wins!")
                    messagebox.showinfo("Result", "You can select as below for power \nSquirtle-Wartortle-Blastoise \nPidget-Pidgeotto-Pidgeot \nBulbasaur-Venusaur-Ivysaur\n Charmeleon-Charmander-Charizard \n Beedrill-Butterfree-Caterpie \n Weedle-Kakuna-Metapod")
                    self.player1_score += 1
                    label_score1.config(text=f"Score: {self.player1_score}")
                    reset_battle()
                else:
                    player_turn = 2
                    toggle_player_turn()

            else:
                self.opponent_health1 = progressbar1_1['value']
                selected_pokemon_row = self.pokemon_game_instance.copied_data[self.pokemon_game_instance.copied_data['Name'] == self.pokemon_game_instance.selected_pokemon1]
                
                # calculation for damage
                player_attack_value = selected_pokemon_row.iloc[0]["Attack"]
                damageable_attack_value = int(random.randint(75, 100)  / 100 * float(player_attack_value))
                
                # calculation for health
                new_health2 = max(self.opponent_health1 - damageable_attack_value, 0)
                is_critical = 1 if new_health1 < 100 else 0
                is_elemental = False
                # collecting data and callimg making the excel file
                self.pokemon_game_instance.collect_battle_data(self.pokemon_game_instance.selected_pokemon1,
                                                               self.pokemon_game_instance.selected_pokemon2,
                                                               damageable_attack_value,
                                                               (damageable_attack_value * 0.8),
                                                               new_health1,
                                                               new_health2,
                                                               is_critical,
                                                               is_critical,
                                                               is_elemental,
                                                               is_critical)
                
                print(f"Player 1's {new_health2}/{self.max_health1}")
                
                self.health_label1 = tk.Label(self.labelFrame, text=f"{new_health2}/{self.max_health2}",  font=('Times New Roman', 8, 'bold'))
                self.health_label1.grid(row=4, column=0)
                progressbar1_1['value'] = new_health2
                
                if new_health2 == 0:
                    self.max_health1 += 25
                    messagebox.showinfo("Result", "Player 2 wins!")
                    messagebox.showinfo("Result", "You can select as below for power \nSquirtle-Wartortle-Blastoise \nPidget-Pidgeotto-Pidgeot \nBulbasaur-Venusaur-Ivysaur\n Charmeleon-Charmander-Charizard \n Beedrill-Butterfree-Caterpie \n Weedle-Kakuna-Metapod")
                    self.player2_score += 1
                    label_score2.config(text=f"Score: {self.player2_score}")
                    reset_battle()
                else:
                    player_turn = 1
                    toggle_player_turn()  


        # elemental attack button modifications
        def attack_elemental():
            new_health1 = 0
            new_health2 = 0
            nonlocal player_turn
            if player_turn == 1:
                if self.player1_score >= 1:
                    self.opponent_health2 = progressbar2_1['value']
                    
                    
                    # calculation for damage
                    selected_pokemon_row = self.pokemon_game_instance.copied_data[self.pokemon_game_instance.copied_data['Name'] == self.pokemon_game_instance.selected_pokemon1]
                    player_attack_value = selected_pokemon_row.iloc[0].get("Attack", 0)
                    damageable_attack_value = int(random.randint(50, 100) / 100 * float(player_attack_value) * 0.8)
                    
                    # calculation for health
                    new_health1 = max(self.opponent_health2 - damageable_attack_value, 0)
                    is_critical = 1 if new_health1 < 100 else 0
                    is_elemental = True
                # collecting data and callimg making the excel file
                    self.pokemon_game_instance.collect_battle_data(self.pokemon_game_instance.selected_pokemon1,
                                                               self.pokemon_game_instance.selected_pokemon2,
                                                               damageable_attack_value,
                                                               (damageable_attack_value * 0.8),
                                                               new_health1,
                                                               new_health2,
                                                               is_critical,
                                                               is_critical,
                                                               is_elemental,
                                                               is_critical)
                        
                    print(f"Player 2's {new_health1}")
                else:
                    self.opponent_health2 = progressbar2_1['value']
                    selected_pokemon_row = self.pokemon_game_instance.copied_data[self.pokemon_game_instance.copied_data['Name'] == self.pokemon_game_instance.selected_pokemon1]
                    
                    
                    # calculation for damage
                    player_attack_value = selected_pokemon_row.iloc[0].get("Attack", 0)
                    damageable_attack_value = int(random.randint(50, 100) / 100 * float(player_attack_value))
                    
                    # calculation for health
                    new_health1 = max(self.opponent_health2 - damageable_attack_value, 0)
                    is_critical = 1 if new_health1 < 100 else 0
                    is_elemental = True
                    
                    # collecting data and callimg making the excel file
                    self.pokemon_game_instance.collect_battle_data(self.pokemon_game_instance.selected_pokemon1,
                                                               self.pokemon_game_instance.selected_pokemon2,
                                                               damageable_attack_value,
                                                               (damageable_attack_value * 0.8),
                                                               new_health1,
                                                               new_health1,
                                                               is_critical,
                                                               is_critical,
                                                               is_elemental,
                                                               is_critical)
                    print(f"Player 2's {new_health1}")

                self.health_label2 = tk.Label(self.labelFrame, text=f"{new_health1}/{self.max_health1}", font=('Times New Roman', 8, 'bold'))
                self.health_label2.grid(row=4, column=1)

                progressbar2_1['value'] = new_health1

                if new_health1 == 0:
                    self.max_health2 += 25
                    messagebox.showinfo("Result", "Player 1 wins!")
                    self.player1_score += 1
                    label_score1.config(text=f"Score: {self.player1_score}")
                    reset_battle()
                else:
                    player_turn = 2
                    toggle_player_turn()

            else:
                if self.player2_score >= 1:
                    self.opponent_health1 = progressbar1_1['value']
                    
                    # calculation for damage
                    selected_pokemon_row = self.pokemon_game_instance.copied_data[self.pokemon_game_instance.copied_data['Name'] == self.pokemon_game_instance.selected_pokemon2]
                    player_attack_value = selected_pokemon_row.iloc[0].get("Attack", 0)
                    damageable_attack_value = int(random.randint(50, 100) / 100 * float(player_attack_value) * 0.8)
                    
                    # calculation for health
                    new_health2 = max(self.opponent_health1 - damageable_attack_value, 0)
                    is_critical = 1 if new_health1 < 100 else 0
                    is_elemental = True
                    
                    
                    # collecting data and callimg making the excel file
                    self.pokemon_game_instance.collect_battle_data(self.pokemon_game_instance.selected_pokemon1,
                                                               self.pokemon_game_instance.selected_pokemon2,
                                                               damageable_attack_value,
                                                               (damageable_attack_value * 0.8),
                                                               new_health1,
                                                               new_health2,
                                                               is_critical,
                                                               is_critical,
                                                               is_elemental,
                                                               is_critical)
                    print(f"Player 1's {new_health2}")
                else:
                    self.opponent_health1 = progressbar1_1['value']
                    
                    # calculation for damage
                    selected_pokemon_row = self.pokemon_game_instance.copied_data[self.pokemon_game_instance.copied_data['Name'] == self.pokemon_game_instance.selected_pokemon2]
                    player_attack_value = selected_pokemon_row.iloc[0].get("Attack", 0)
                    damageable_attack_value = int(random.randint(50, 100) / 100 * float(player_attack_value))
                    
                    # calculation for health
                    new_health2 = max(self.opponent_health1 - damageable_attack_value, 0)
                    is_critical = 1 if new_health1 < 100 else 0
                    is_elemental = True
                    
                    
                    # collecting data and callimg making the excel file
                    self.pokemon_game_instance.collect_battle_data(self.pokemon_game_instance.selected_pokemon1,
                                                               self.pokemon_game_instance.selected_pokemon2,
                                                               damageable_attack_value,
                                                               (damageable_attack_value * 0.8),
                                                               new_health1,
                                                               new_health2,
                                                               is_critical,
                                                               is_critical,
                                                               is_elemental,
                                                               is_critical)
                    
                    print(f"Player 1's {new_health2}")

                self.health_label1 = tk.Label(self.labelFrame, text=f"{new_health2}/{self.max_health2}", font=('Times New Roman', 8, 'bold'))
                self.health_label1.grid(row=4, column=0)

                progressbar1_1['value'] = new_health2

                if new_health2 == 0:
                    self.max_health1 += 25
                    messagebox.showinfo("Result", "Player 2 wins!")
                    self.player2_score += 1
                    label_score2.config(text=f"Score: {self.player2_score}")
                    reset_battle()
                else:
                    player_turn = 1
                    toggle_player_turn()

         #
        
        # toogling the player turns 
        def toggle_player_turn():
            if player_turn == 1:
                # disabling the buttons
                button_physical2.config(state=tk.DISABLED)
                button_elemental2.config(state=tk.DISABLED)
                button_physical1.config(state=tk.NORMAL)
                button_elemental1.config(state=tk.NORMAL)
                label_turn.config(text="Player 1's Turn")
            else:
                # disabling the buttons
                button_physical1.config(state=tk.DISABLED)
                button_elemental1.config(state=tk.DISABLED)
                button_physical2.config(state=tk.NORMAL)
                button_elemental2.config(state=tk.NORMAL)
                label_turn.config(text="Player 2's Turn")
                

            # for resetting the game and ending
        

        # resetting and ending the game
        def reset_battle():
            
            # setting prograssbar value
            progressbar1_1['value'] = self.max_health1
            progressbar2_1['value'] = self.max_health2
            
            if self.player1_score == 3:
                self.pokemon_game_instance.write_battle_data_to_excel()
                messagebox.showinfo("Game Over", "Player 1 wins the game!\nPlease close each Matplotlib Window to see the next one.")
                root.destroy()
                visualize()
                                
            elif self.player2_score == 3:
                self.pokemon_game_instance.write_battle_data_to_excel()
                messagebox.showinfo("Game Over", "Player 2 wins the game!\nPlease close each Matplotlib Window to see the next one.")
                root.destroy()
                visualize()
                    
                            
            if self.player1_score == 1 or self.player1_score == 2:
                    self.pokemon_game_instance.evolve_pokemon(1)
                    # once condition is met calling again
                    self.selected_pokemon2 = self.pokemon_game_instance.choose_pokemon_gui(score1=self.player1_score, score2=self.player2_score, health1=self.max_health1, health2=self.max_health2)
                    
            if self.player2_score == 1 or self.player2_score == 2:
                    self.pokemon_game_instance.evolve_pokemon(2)
                    # once condition is met calling again
                    self.selected_pokemon1 = self.pokemon_game_instance.choose_pokemon_gui(score1=self.player1_score, score2=self.player2_score, health1=self.max_health1, health2=self.max_health2)
                    
            player_turn = random.randint(1, 2)
            toggle_player_turn()
            self.root.destroy()

                
        # def display_selected_pokemon():
        #     # Display selected Pokemon images
        #     if self.pokemon_game_instance.selected_pokemon1:
        #         image_path1 = f"D:\\Coding\\PythonVScode\\PokemonProject\\Images\\.png"
        #         image1 = Image.open(image_path1)
        #         resized_image1 = image1.resize((170, 170))
        #         self.image1_tk = ImageTk.PhotoImage(resized_image1)
        #         self.image_label1.config(image=self.image1_tk)
        #         self.image_references.append(self.image1_tk)  # Store image reference
                
        #     if self.pokemon_game_instance.selected_pokemon2:
        #         image_path2 = f"D:\\Coding\\PythonVScode\\PokemonProject\\Images\\none.png"
        #         image2 = Image.open(image_path2)
        #         resized_image2 = image2.resize((170, 170))
        #         self.image2_tk = ImageTk.PhotoImage(resized_image2)
        #         self.image_label2.config(image=self.image2_tk)
        #         self.image_references.append(self.image2_tk)
        
        
        root = tk.Tk()
        root.title("Pokemon Battle")

        self.frame = tk.Frame(root)
        self.labelFrame = tk.LabelFrame(self.frame)
        self.labelFrame.grid(row=0, column=0)

        # player 1 title
        self.name1 = tk.Label(self.labelFrame, text="Player 1")
        self.name1.grid(row=0, column=0, padx=70)
        
        # player 2 title
        self.name2 = tk.Label(self.labelFrame, text="Player 2")
        self.name2.grid(row=0, column=1, padx=70)
        
        # self.image_label1 = tk.Label(self.labelFrame)
        # self.image_label1.grid(row=7, column=0)  # Player 1 image
        # display_selected_pokemon()

        # self.image_label2 = tk.Label(self.labelFrame)
        # self.image_label2.grid(row=7, column=1)
        # self.display_selected_pokemon()         
        
        
        def visualize():
            battle_data = pd.read_excel("D:\\Coding\\PythonVScode\\battle_data.xlsx")
            
            # pokemon 1 and damage 1 visualization
            plt.figure(figsize=(7, 6))
            plt.bar(battle_data["Pokemon 1"], battle_data["Damage 1"])
            plt.xlabel("Pokemon")
            plt.ylabel("Damage")
            plt.title("Damage Dealt by Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            # pokemon 2 and damage 1 visualization
            plt.figure(figsize=(7, 6))
            plt.bar(battle_data["Pokemon 2"], battle_data["Damage 1"])
            plt.xlabel("Pokemon")
            plt.ylabel("Damage")
            plt.title("Damage Dealt by Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            
            # pokemon 1 and damage 2 visualization
            plt.figure(figsize=(7, 6))
            plt.bar(battle_data["Pokemon 1"], battle_data["Damage 2"])
            plt.xlabel("Pokemon")
            plt.ylabel("Damage")
            plt.title("Damage Dealt by Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            
            
            
            # pokemon 1 and damage 2 visualization
            plt.figure(figsize=(7, 6))
            plt.bar(battle_data["Pokemon 1"], battle_data["Damage 2"])
            plt.xlabel("Pokemon")
            plt.ylabel("Damage")
            plt.title("Damage Dealt by Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            
            # damage 1 visualization
            plt.figure(figsize=(7, 6))
            plt.plot(battle_data["Damage 1"], color='g')
            plt.xlabel("Pokemon")
            plt.ylabel("Damage")
            plt.title("Damage Dealt by Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            
            # damage 2 visualization
            plt.figure(figsize=(7, 6))
            plt.plot(battle_data["Damage 2"], color='r')
            plt.xlabel("Pokemon")
            plt.ylabel("Damage")
            plt.title("Damage Dealt by Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            # health 1 visualization
            plt.figure(figsize=(7, 6))
            plt.plot(battle_data["Health 1"], color='b')
            plt.xlabel("Pokemon")
            plt.ylabel("Damage")
            plt.title("Damage Dealt by Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            
            # health 2 visualization
            plt.figure(figsize=(7, 6))
            plt.plot(battle_data["Health 2"], color='b')
            plt.xlabel("Pokemon")
            plt.ylabel("Damage")
            plt.title("Damage Dealt by Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            
            

            # pokemon and health visualization
            plt.figure(figsize=(7, 6))
            plt.bar(battle_data["Pokemon 1"], battle_data["Health 1"])
            plt.xlabel("Pokemon")
            plt.ylabel("Health")
            plt.title("Remaining Health of Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

            # plot the critical Hits
            critical = battle_data.groupby("Pokemon 1")["Critical 1"].sum().reset_index()
            plt.figure(figsize=(7, 6))
            plt.bar(critical["Pokemon 1"], critical["Critical 1"], color='maroon')
            plt.xlabel("Pokemon")
            plt.ylabel("Critical Hits")
            plt.title("Critical Hits by Each Pokemon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        
        # score 1
        self.score1 = tk.Label(self.labelFrame, text=f"Score: {self.player1_score}")
        self.score1.grid(row=1, column=0)
        label_score1 = self.score1

        # score 2
        self.score2 = tk.Label(self.labelFrame, text=f"Score: {self.player2_score}")
        self.score2.grid(row=1, column=1)
        label_score2 = self.score2

        # turn indicator
        player_turn = random.randint(1, 2)
        label_turn = tk.Label(self.labelFrame, text=f"Player {player_turn}'s Turn")
        label_turn.grid(row=2, columnspan=2)

        # progress bar for player 1
        progressbar1_1 = ttk.Progressbar(self.labelFrame, orient='horizontal', mode='determinate', length=100)
        progressbar1_1.grid(row=3, column=0, padx=5, pady=5)
        progressbar1_1['value'] = self.max_health1
        progressbar1_1['maximum'] = self.max_health1
        

        
        
        # progress bar for player 2
        progressbar2_1 = ttk.Progressbar(self.labelFrame, orient='horizontal', mode='determinate', length=100)
        progressbar2_1.grid(row=3, column=1, padx=5, pady=5)
        progressbar2_1['value'] = self.max_health2
        progressbar2_1['maximum'] = self.max_health2
        
        #printing the results for testing
        print(self.pokemon_game_instance.selected_pokemon1)
        print(self.pokemon_game_instance.selected_pokemon2)


        

        # physical attack button for player 1
        button_physical1 = ttk.Button(self.labelFrame, text="Physical Attack", command=attack_physical)
        button_physical1.grid(row=6, column=0, padx=5, pady=5)

        # elemental attack button for player 1
        button_elemental1 = ttk.Button(self.labelFrame, text="Elemental Attack", command=attack_elemental)
        button_elemental1.grid(row=7, column=0, padx=5, pady=5)

        # physical attack button for player 2
        button_physical2 = ttk.Button(self.labelFrame, text="Physical Attack", command=attack_physical)
        button_physical2.grid(row=6, column=1, padx=5, pady=5)

        # elemental attack button for player 2
        button_elemental2 = ttk.Button(self.labelFrame, text="Elemental Attack", command=attack_elemental)
        button_elemental2.grid(row=7, column=1, padx=5, pady=5)
        

        toggle_player_turn()
        self.frame.pack()
        root.mainloop()




pokemon_game_instance = PokemonGame()
pokemon_game_instance.dataCleaning()
pokemon_game_instance.choose_pokemon_gui()
