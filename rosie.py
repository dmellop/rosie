from sys import argv


def entered_command(argv):
    if len(argv) >= 2:
        return argv[1]
    return None


def help():
    message = (
        'Usages:',
        '  python rosie.py run',
        '  python rosie.py run <path to output directory>',
        '  python rosie.py test',
    )
    print('\n'.join(message))


def run():
    import rosie
    target_directory = argv[2] if len(argv) >= 3 else '/tmp/serenata-data/'
    rosie.main(target_directory)


def test():
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)


commands = {'run': run, 'test': test}
command = commands.get(entered_command(argv), help)
command()
