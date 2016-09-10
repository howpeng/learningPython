def save_float(obj):
    try:
        return float(obj)
    except ValueError:
        print('value error hahahah')
    except IOError:
        print('IOeeeeeeeee')


save_float('asdfs')