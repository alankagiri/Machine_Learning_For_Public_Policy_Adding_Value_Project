columns_to_exclude = ['create_date_utc','closed_date_utc','last_action_utc', 'cross_street']
# Justification for dropped columns:
    # The columns with '_utc' endings have the Eastern Time zone equivalent, and add little value to analysis, 
    # expecially in ML settings where such redudancies can lead to multicollinearity

    # The 'cross_street' column has 90% of its values missing