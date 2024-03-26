help :- 
    write('Analyse the upcoming diseases:'), nl,
    write('skin.'), nl,
    write('heart.'), nl,
    write('ent.'), nl,
    write('skeleton.'), nl.

skin :- 
    write('Does any itching occur? (yes/no)'), nl,
    read(Ans),
    (   Ans = yes -> 
        write('Apply the cream preferred by the pharmacist.');
        Ans = no -> 
        (   write('Did any patches form? (yes/no)'), nl,
            read(Patch),
            (   Patch = yes -> 
                write('Consult the dermatologist.');
                Patch = no -> 
                (   write('Did you face this problem before? (yes/no)'), nl,
                    read(Previous),
                    (   Previous = yes -> 
                        write('Immediately seek treatment.');
                        Previous = no -> 
                        write('No specific action required.'))
                )
            )
        )
    ).

heart :- 
    write('Do you have any blocks in the heart? (yes/no)'), nl,
    read(Blocks),
    (   Blocks = yes -> 
        write('Do regular cardiovascular exercises.');
        Blocks = no -> 
        (   write('Did you have any heart attacks previously? (yes/no)'), nl,
            read(Attacks),
            (   Attacks = yes -> 
                write('Consult a cardiologist.');
                Attacks = no -> 
                (   write('Did you undergo any heart operations? (yes/no)'), nl,
                    read(Operations),
                    (   Operations = yes -> 
                        write('Consult with the same doctor.');
                        Operations = no -> 
                        (   write('Are you over 50 years old? (yes/no)'), nl,
                            read(Age),
                            (   Age = yes -> 
                                write('Do not strain and take complete rest.');
                                Age = no -> 
                                write('No specific action required.'))
                        )
                    )
                )
            )
        )
    ).

ent :- 
    write('Do you have any illness in the ear? (yes/no)'), nl,
    read(EarIllness),
    (   EarIllness = yes -> 
        write('Clean the ears with earbuds.');
        EarIllness = no -> 
        (   write('Did you meet with any accidents on the top of the head? (yes/no)'), nl,
            read(HeadAccidents),
            (   HeadAccidents = yes -> 
                write('Check whether blood comes from the ears.');
                HeadAccidents = no -> 
                (   write('Do you have any illness in the nose? (yes/no)'), nl,
                    read(NoseIllness),
                    (   NoseIllness = yes -> 
                        write('Practice regular breathing exercises.');
                        NoseIllness = no -> 
                        (   write('Do you have any illness in the throat? (yes/no)'), nl,
                            read(ThroatIllness),
                            (   ThroatIllness = yes -> 
                                write('Gargle with hot water and salt.');
                                ThroatIllness = no -> 
                                (   write('Do you have thyroid problems? (yes/no)'), nl,
                                    read(Thyroid),
                                    (   Thyroid = yes -> 
                                        write('Consult ENT specialists and follow proper treatments.');
                                        Thyroid = no -> 
                                        (   write('Do you have frequent colds? (yes/no)'), nl,
                                            read(Cold),
                                            (   Cold = yes -> 
                                                write('Try to drink hot water until it is cured.');
                                                Cold = no -> 
                                                (   write('Do you have a dry cough? (yes/no)'), nl,
                                                    read(DryCough),
                                                    (   DryCough = yes -> 
                                                        write('Take dry cough syrups.');
                                                        DryCough = no -> 
                                                        (   write('Do you have a cold cough? (yes/no)'), nl,
                                                            read(ColdCough),
                                                            (   ColdCough = yes -> 
                                                                write('Take cold cough syrups.');
                                                                ColdCough = no -> 
                                                                write('No specific action required.')
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    ).

skeleton :- 
    write('Did you meet with any accidents? (yes/no)'), nl,
    read(Accidents),
    (   Accidents = yes -> 
        write('Check for any skeletal damages.');
        Accidents = no -> 
        (   write('Did you have any plates inserted in your body? (yes/no)'), nl,
            read(Plates),
            (   Plates = yes -> 
                write('Be careful with your movements.');
                Plates = no -> 
                (   write('Do you have any artificial body parts? (yes/no)'), nl,
                    read(ArtificialParts),
                    (   ArtificialParts = yes -> 
                        write('Use them with proper care.');
                        ArtificialParts = no -> 
                        write('No specific action required.')
                    )
                )
            )
        )
    ).

start :-
    help,
    analyze.

analyze :-
    write('Enter the area to analyze:'), nl,
    read(Area),
    (   Area = skin -> skin;
        Area = heart -> heart;
        Area = ent -> ent;
        Area = skeleton -> skeleton;
        write('Invalid area. Please try again.'), nl,
        analyze
    ).

