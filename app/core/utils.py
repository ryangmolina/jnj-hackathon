def get_app_name(entity_model_name):
    last_letter = entity_model_name[-1]

    if last_letter == 'y':
        app_name = '{}ies'.format(entity_model_name[:-1])
    else:
        app_name = '{}s'.format(entity_model_name)

    return app_name
