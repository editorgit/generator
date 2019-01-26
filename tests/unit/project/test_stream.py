from zmei_generator.contrib.channels.extras.pages.stream import StreamPageExtra
from zmei_generator.generator.application import ZmeiProject, ZmeiProjectParser


def test_simple_reuse_another_app():

    app_parser = ZmeiProjectParser()
    app_parser.add_file('main.col', """    
        @channels
        
        [bar: /bar]
        @react {}
        @stream(
            #another.foo
            #another.boo
        )
    """)

    app_parser.add_file('another.col', """    
        #foo
        --------
        foo
        
        #boo
        --------
        boo
    """)

    project = app_parser.parse()

    assert isinstance(project, ZmeiProject)

    main_app = project.get_application('main')
    another_app = project.get_application('another')

    assert main_app.application is project
    assert main_app.app_name == 'main'
    assert another_app.application is project
    assert another_app.app_name == 'another'

    assert len(main_app.pages) == 1

    bar = main_app.pages['bar']

    assert isinstance(bar.stream, StreamPageExtra)

    assert bar.stream.models[0].target == 'Foo'
    assert bar.stream.models[1].target == 'Boo'
