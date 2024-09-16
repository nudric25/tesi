def computer_stops(ais):
    ais=ais[['SOG','IMO','LATITUDE','LONGITUDE']]

    # Crea la colonna 'is_stop' basata sulla velocità
    ais['is_stop'] = ais['SOG'] < 3

    # Inizializza una lista per memorizzare i dati degli stop
    stop_data = []
    current_stop = None
    count = 0

    # Itera attraverso il DataFrame per identificare e contare gli stop consecutivi
    for index, row in ais.iterrows():
        if row['is_stop']:
            count += 1
            if current_stop is None:
                current_stop = row.copy()  # Inizia un nuovo stop
        else:
            if current_stop is not None:
                # Aggiungi il blocco di stop al DataFrame
                current_stop['DURATION'] = count
                stop_data.append(current_stop)
                current_stop = None
                count = 0

    # Aggiungi l'ultimo stop se il DataFrame termina con uno stop
    if current_stop is not None:
        current_stop['DURATION'] = count
        stop_data.append(current_stop)

    # Crea un DataFrame dai risultati
    stops = pd.DataFrame(stop_data)
    stops=stops[['IMO','LONGITUDE','LATITUDE','DURATION']]
    return stops
