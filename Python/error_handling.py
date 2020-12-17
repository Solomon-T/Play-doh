# use try, except, break
# not once one of the exeptions is hit, it doent check for the other exceptions

while True:
    try:
        age = int(input('what is your age?'))
        print(age/10)
        raise Exception('Hey cut it oyt')
    except ValueError:
        print('please enter a number')
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError as err:
        # print('please enter a number other than zero' + err) you cant add 
        print(f'{err}')
        print(err) # err is an object
    except (ZeroDivisionError, ValueError) as errs: # Catching more than one error
        print(errs)
    except:
        print("some other error")
    else:
        print('You are just too old for me.')
        break
    finally:
        print('this always run even if there is an error')
     
