class Diseases:
    def __init__(self):
        self.all_info = [['Anaplasmosis',
                          'Anaplasmosis is a vector-borne, infectious blood disease in cattle caused by the rickesttsial ' \
                          'parasites Anaplasma marginale and Anaplasma centrale. It is also known as yellow-bag or ' \
                          'yellow-fever. This parasite infects the red blood cells and causes severe anemia. It is most ' \
                          'usually spread by ticks.', ['Anemia',
                                                       'Fever',
                                                       'Weight loss',
                                                       'Breathlessness',
                                                       'Jaundice',
                                                       'Uncoordinated movements',
                                                       'Abortion',
                                                       'Death'],
                          'Tetracycline is often used for clinical anaplasmosis. However it cannot be used in every ' \
                          'country. General supportive care is also important for anemic animals. Blood transfusions are of ' \
                          'limited benefit. The incubation time for the disease to develop varies from two weeks to over ' \
                          'three months, but averages three to four weeks. Adult cattle are more susceptible to infection ' \
                          'than calves. The disease is generally mild in calves under a year of age, rarely fatal in cattle ' \
                          'up to two years of age, sometimes fatal in animals up to three years of age, and often fatal in ' \
                          'older cattle. Once an animal recovers from infection, either naturally or with normal therapy, ' \
                          'it will usually remain a carrier of the disease for life. Carriers show no sign of the disease ' \
                          'but act as sources of infection for other susceptible cattle. '],

                         ['Anthrax',
                          'Anthrax, a highly infectious and fatal disease of mammals and humans, is caused by a ' \
                          'relatively large spore-forming rectangular shaped bacterium called Bacillus anthracis. Anthrax ' \
                          'is found on all the continents, causes acute mortality in ruminants and is a zoonosis. The ' \
                          'bacteria produce extremely potent toxins which are responsible for the ill effects, ' \
                          'causing a high mortality rate. While most mammals are susceptible, anthrax is typically a ' \
                          'disease of ruminants and humans. It does not typically spread from animal to animal nor from ' \
                          'person to person. The bacteria produce spores on contact with oxygen. ',
                          [
                              'Sudden death within within 2 or 3 hours of being apparently normal',
                              'Occasional trembling',
                              'High temperature',
                              'Difficulty in breathing',
                              'Collapse and convulsions before death.',
                              'Blood not cloting after death, resulting in a small amount of bloody discharge from the nose, '
                              'mouth and other openings'],
                          'Due to the rapidity of the disease treatment is seldom possible, although high doses of ' \
                          'penicillin have been effective in the later stages of some outbreaks. '],

                         ['Babesisosis',
                          'Bovine Babesiosis (BB) is a tick-borne disease of cattle. The principal strains are babesia ' \
                          'bovis and babesia bigemina, with Rhipicephalus ticks being the major vector. Babesia divergens ' \
                          'is also found, with the major vector being Ixodes ricinus. BB is found in areas where its ' \
                          'arthropod vector is distributed, especially tropical and subtropical climates. Babesia bovis ' \
                          'and B. bigemina are more widely distributed and of major importance in Africa, Asia, ' \
                          'Australia, and Central and South America. Babesia divergens is economically important in some ' \
                          'parts of Europe and possibly northern Africa. Transmission of B bovis takes place when ' \
                          'engorging adult female ticks pick up the infection. They pass it on to their progeny via their ' \
                          'eggs. Larvae (or seed ticks) then pass it on in turn when feeding on another animal. B ' \
                          'bigemina is also passed from one generation of ticks to the next. Engorging adult ticks pick ' \
                          'up the infection and nymphal and adult stages (not larval stages) of the next generation pass ' \
                          'it on to other cattle. Morbidity and mortality vary greatly and are influenced by prevailing ' \
                          'treatments employed in an area, previous exposure to a species/strain of parasite, ' \
                          'and vaccination status. In endemic areas, cattle become infected at a young age and develop a ' \
                          'long-term immunity. However, outbreaks can occur in these endemic areas if exposure to ticks ' \
                          'by young animals is interrupted or immuno-naïve cattle are introduced. The introduction of ' \
                          'Babesia infected ticks into previously tick-free areas may also lead to outbreaks of disease. ',
                          [],
                          'Mild cases may recover without treatment. Sick animals can be treated with an antiparasitic ' \
                          'drug. Treatment is most likely to be successful if the disease is diagnosed early; it may fail ' \
                          'if the animal has been weakened by anemia. Imidocarb has been reported to protect animals from ' \
                          'disease but immunity can develop. There are also concerns with regard to residues in milk and ' \
                          'meat. In some cases blood transfusions and other supportive therapy should be considered. '],

                         ['Blue tongue',
                          'Bluetongue disease is a noncontagious, insect-borne, viral disease of ruminants, mainly sheep ' \
                          'and less frequently cattle, goats, buffalo, deer, dromedaries, and antelope. It is caused by ' \
                          'Bluetongue virus (BTV). The virus is transmitted by the midges Culicoides imicola, Culicoides ' \
                          'variipennis, and other culicoids. Affected cattle are febrile (up to 40.0°C) and appear stiff ' \
                          'due to swelling of the coronary band at the top of the hooves (coronary band) and are very ' \
                          'reluctant to move. There is a serous to mucopurulent nasal discharge and erosions on the ' \
                          'muzzle with sloughing of the mucosa. There is lacrimation but no obvious eye lesions. ' \
                          'Mortality rates are usually much lower in cattle than in sheep. ', ['Fever up to (40.0ºC)',
                                                                                               'Nasal discharge',
                                                                                               'Swelling of the head and neck',
                                                                                               'Conjunctivitis (runny eyes)',
                                                                                               'Swelling in, and ulceration of the mouth',
                                                                                               'Swollen teats',
                                                                                               'Saliva drooling out of the mouth',
                                                                                               'Abortion'],
                          'Diagnosis is based upon clinical signs, virus detection via PCR and/or seroconversion to ' \
                          'bluetongue virus. Treatment is limited to antibiotic therapy to control secondary bacterial ' \
                          'infections. '],

                         ['Foot and mouth',
                          'Foot-and-mouth disease (FMD) is a severe, highly contagious viral disease of cattle and swine. ' \
                          'It also affects sheep, goats, deer, and other cloven-hooved ruminants. FMD is not recognised ' \
                          'as a zoonotic disease. The disease spreads very quickly if not controlled and because of this ' \
                          'is a reportable disease. The disease is caused by a virus of which there are seven types, ' \
                          'each producing the same symptoms, and distinguishable only in the laboratory. Immunity to one ' \
                          'type does not protect an animal against other types. The interval between exposure to ' \
                          'infection and the appearance of symptoms varies between twenty-four hours and ten days, ' \
                          'or even longer. The average time, under natural conditions, is three to six days. The virus ' \
                          'survives in lymph nodes and bone marrow at neutral pH, but is destroyed in muscle when pH is ' \
                          'less than 6.0, i.e., after rigor mortis. The virus can persist in contaminated fodder and the ' \
                          'environment for up to one month, depending on the temperature and pH conditions. Airborne ' \
                          'spread of the disease can take place and under favourable weather conditions the disease may ' \
                          'be spread considerable distances by this route. Animals pick up the virus either by direct ' \
                          'contact with an infected animal or by contact with foodstuffs or other things which have been ' \
                          'contaminated by such an animal, or by eating or coming into contact with some part of an ' \
                          'infected carcase. Outbreaks have been linked with the importation of infected meat and meat ' \
                          'products. The disease can also be spread by people, vehicles and other objects that have been ' \
                          'contaminated by the virus. ', ['Fever',
                                                          'Blisters in the mouth and on feet',
                                                          'Drop in milk production',
                                                          'Weight loss',
                                                          'Loss of appetite',
                                                          'Quivering lips and frothing of mouth',
                                                          'Cows may develop blisters on teats',
                                                          'Lameness'],
                          'Treatment is not given. Affected animals will recover. However because of the loss of production ' \
                          'and the infectious state of the disease, infected animals are usually culled. '],

                         ['Lumpy skin',
                          'Lumpy skin disease is an infectious, eruptive, occasionally fatal disease of cattle ' \
                          'characterized by nodules on the skin and other parts of the body. Secondary bacterial ' \
                          'infection often aggravates the condition. Lumpy skin disease (LSD) is caused by infection of ' \
                          'cattle or water buffalo with the poxvirus Lumpy skin disease virus (LSDV). The virus is one of ' \
                          'three closely related species within the genus capripoxvirus, the other two species being ' \
                          'Sheeppox virus and Goatpox virus There is still a good deal of information lacking about the ' \
                          'transmission of LSD. Experimental work has shown that direct transmission from an infected to ' \
                          'a naïve animal is very inefficient. Evidence to date supports transmission of the virus via ' \
                          'arthropods such as insects or ticks (these are termed virus "vectors"). For example outbreaks ' \
                          'of LSD occur during warm, wet weather while the disease usually diminishes in the cooler ' \
                          'winter months. In addition, LSD epidemics are often characterised by new outbreaks occurring ' \
                          'at distances over 50km from the nearest known disease focus. These characteristics strongly ' \
                          'suggest insect-borne transmission, such as mosquitoes and ticks. However, it is unclear which ' \
                          'vector species are involved in transmission of LSD, and if it is a simple mechanical ' \
                          'transmission of the virus or a more complicated biological transmission involving replication ' \
                          'or development of the virus in the vector. Movement of infected cattle can also be a ' \
                          'significant factor in the spread of LSD over large distances. ', ['general malaise',
                                                                                             ' ocular and nasal discharge',
                                                                                             ' fever',
                                                                                             'sudden decrease in milk production.',
                                                                                             'Develops nodules which can be difficult to spot. Others develop innumerable nodules up to 3cm in '
                                                                                             'diameter',
                                                                                             'fever and milk drop ',
                                                                                             'with many other diseases.'],
                          'There is no treatment for the virus, so prevention by vaccination is the most effective means of ' \
                          'control.Secondary infections in the skin may be treated with Non-Steroidal Anti-Inflammatories (' \
                          'NSAIDs) and also antibiotics (topical +/- injectable) when appropriate. ']
            , ['', [], '', '']]
