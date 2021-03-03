enc_dict = {'Age': {'20': 20,
                    '24': 24,
                    '22': 22,
                    '27': 27,
                    '23': 23,
                    '21': 21,
                    '28': 28,
                    '25': 25,
                    '32': 32,
                    '30': 30,
                    '31': 31,
                    '26': 26,
                    '18': 18,
                    '19': 19,
                    '33': 33,
                    '29': 29},
            'Gender': {'Female': 0, 'Male': 1},
            'Marital Status': {'Single': 2, 'Married': 0, 'Prefer not to say': 1},
            'Occupation': {'Student': 3,
                           'Employee': 0,
                           'Self Employeed': 2,
                           'House wife': 1},
            'Monthly Income': {'No Income': 4,
                               'Below Rs.10000': 2,
                               'More than 50000': 3,
                               '10001 to 25000': 0,
                               '25001 to 50000': 1},
            'Educational Qualifications': {'Post Graduate': 2,
                                           'Graduate': 0,
                                           'Ph.D': 1,
                                           'Uneducated': 4,
                                           'School': 3},
            'Family size': {4: 4, 3: 3, 6: 6, 2: 2, 5: 5, 1: 1},
            'Medium (P1)': {'Food delivery apps': 1,
                            'Walk-in': 2,
                            'Direct call': 0,
                            'Web browser': 3},
            'Medium (P2)': {' Web browser': 2, ' Direct call': 0, ' Walk-in': 1},
            'Meal(P1)': {'Breakfast': 0, 'Snacks': 3, 'Lunch': 2, 'Dinner': 1},
            'Meal(P2)': {' Lunch': 1, ' Dinner': 0, ' Snacks': 2},
            'Perference(P1)': {'Non Veg foods (Lunch / Dinner)': 1,
                               'Veg foods (Breakfast / Lunch / Dinner)': 3,
                               'Bakery items (snacks)': 0,
                               'Sweets': 2},
            'Perference(P2)': {' Bakery items (snacks)': 0,
                               ' Veg foods (Breakfast / Lunch / Dinner)': 3,
                               ' Ice cream / Cool drinks': 1,
                               ' Sweets': 2},
            'Ease and convenient': {'Neutral': 2,
                                    'Strongly agree': 3,
                                    'Agree': 0,
                                    'Strongly disagree': 4,
                                    'Disagree': 1},
            'Time saving': {'Neutral': 2,
                            'Strongly agree': 3,
                            'Agree': 0,
                            'Disagree': 1,
                            'Strongly disagree': 4},
            'More restaurant choices': {'Neutral': 2,
                                        'Strongly agree': 3,
                                        'Agree': 0,
                                        'Strongly disagree': 4,
                                        'Disagree': 1},
            'Easy Payment option': {'Neutral': 2,
                                    'Strongly agree': 3,
                                    'Agree': 0,
                                    'Disagree': 1,
                                    'Strongly disagree': 4},
            'More Offers and Discount': {'Neutral': 2,
                                         'Strongly agree': 3,
                                         'Agree': 0,
                                         'Disagree': 1,
                                         'Strongly disagree': 4},
            'Good Food quality': {'Neutral': 2,
                                  'Disagree': 1,
                                  'Agree': 0,
                                  'Strongly agree': 3,
                                  'Strongly disagree': 4},
            'Good Tracking system': {'Neutral': 2,
                                     'Agree': 0,
                                     'Strongly agree': 3,
                                     'Disagree': 1,
                                     'Strongly disagree': 4},
            'Self Cooking': {'Neutral': 2,
                             'Strongly agree': 3,
                             'Disagree': 1,
                             'Agree': 0,
                             'Strongly disagree': 4},
            'Health Concern': {'Neutral': 2,
                               'Strongly agree': 3,
                               'Agree': 0,
                               'Strongly disagree': 4,
                               'Disagree': 1},
            'Late Delivery': {'Neutral': 2,
                              'Agree': 0,
                              'Strongly agree': 3,
                              'Disagree': 1,
                              'Strongly disagree': 4},
            'Poor Hygiene': {'Neutral': 2,
                             'Strongly agree': 3,
                             'Agree': 0,
                             'Disagree': 1,
                             'Strongly disagree': 4},
            'Bad past experience': {'Neutral': 2,
                                    'Strongly agree': 3,
                                    'Agree': 0,
                                    'Disagree': 1,
                                    'Strongly disagree': 4},
            'Unavailability': {'Neutral': 2,
                               'Strongly agree': 3,
                               'Agree': 0,
                               'Disagree': 1,
                               'Strongly disagree': 4},
            'Unaffordable': {'Neutral': 2,
                             'Strongly agree': 3,
                             'Agree': 0,
                             'Disagree': 1,
                             'Strongly disagree': 4},
            'Long delivery time': {'Agree': 0,
                                   'Strongly agree': 3,
                                   'Neutral': 2,
                                   'Disagree': 1,
                                   'Strongly disagree': 4},
            'Delay of delivery person getting assigned': {'Agree': 0,
                                                          'Strongly agree': 3,
                                                          'Disagree': 1,
                                                          'Neutral': 2,
                                                          'Strongly disagree': 4},
            'Delay of delivery person picking up food': {'Agree': 0,
                                                         'Strongly agree': 3,
                                                         'Neutral': 2,
                                                         'Disagree': 1,
                                                         'Strongly disagree': 4},
            'Wrong order delivered': {'Agree': 0,
                                      'Strongly agree': 3,
                                      'Disagree': 1,
                                      'Neutral': 2,
                                      'Strongly disagree': 4},
            'Missing item': {'Agree': 0,
                             'Strongly agree': 3,
                             'Disagree': 1,
                             'Neutral': 2,
                             'Strongly disagree': 4},
            'Order placed by mistake': {'Agree': 0,
                                        'Strongly agree': 3,
                                        'Neutral': 2,
                                        'Disagree': 1,
                                        'Strongly disagree': 4},
            'Influence of time': {'Yes': 2, 'No': 1, 'Maybe': 0},
            'Order Time': {'Weekend (Sat & Sun)': 2,
                           'Anytime (Mon-Sun)': 0,
                           'Weekdays (Mon-Fri)': 1},
            'Maximum wait time': {'30 minutes': 1,
                                  '45 minutes': 2,
                                  '60 minutes': 3,
                                  'More than 60 minutes': 4,
                                  '15 minutes': 0},
            'Residence in busy location': {'Agree': 0,
                                           'Strongly Agree': 3,
                                           'Disagree': 1,
                                           'Neutral': 2,
                                           'Strongly disagree': 4},
            'Google Maps Accuracy': {'Neutral': 2,
                                     'Strongly Agree': 3,
                                     'Agree': 0,
                                     'Disagree': 1,
                                     'Strongly disagree': 4},
            'Good Road Condition': {'Neutral': 2,
                                    'Disagree': 1,
                                    'Agree': 0,
                                    'Strongly Agree': 3,
                                    'Strongly disagree': 4},
            'Low quantity low time': {'Neutral': 2,
                                      'Strongly disagree': 4,
                                      'Agree': 0,
                                      'Disagree': 1,
                                      'Strongly Agree': 3},
            'Delivery person ability': {'Neutral': 2,
                                        'Agree': 0,
                                        'Strongly Agree': 3,
                                        'Disagree': 1,
                                        'Strongly disagree': 4},
            'Influence of rating': {'Yes': 2, 'Maybe': 0, 'No': 1},
            'Less Delivery time': {'Moderately Important': 1,
                                   'Very Important': 4,
                                   'Important': 0,
                                   'Slightly Important': 2,
                                   'Unimportant': 3},
            'High Quality of package': {'Moderately Important': 1,
                                        'Very Important': 4,
                                        'Important': 0,
                                        'Unimportant': 3,
                                        'Slightly Important': 2},
            'Number of calls': {'Moderately Important': 1,
                                'Very Important': 4,
                                'Unimportant': 3,
                                'Important': 0,
                                'Slightly Important': 2},
            'Politeness': {'Moderately Important': 1,
                           'Very Important': 4,
                           'Important': 0,
                           'Slightly Important': 2,
                           'Unimportant': 3},
            'Freshness ': {'Moderately Important': 1,
                           'Very Important': 4,
                           'Important': 0,
                           'Slightly Important': 2,
                           'Unimportant': 3},
            'Temperature': {'Moderately Important': 1,
                            'Very Important': 4,
                            'Important': 0,
                            'Slightly Important': 2,
                            'Unimportant': 3},
            'Good Taste ': {'Moderately Important': 1,
                            'Very Important': 4,
                            'Important': 0,
                            'Slightly Important': 2,
                            'Unimportant': 3},
            'Good Quantity': {'Moderately Important': 1,
                              'Very Important': 4,
                              'Important': 0,
                              'Slightly Important': 2,
                              'Unimportant': 3},
            'Output': {'Yes': 1, 'No': 0}}