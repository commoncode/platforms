from setuptools import setup, find_packages

setup( name='platforms',
    version = '0.0.3',
    description = 'Platforms for Django',
    author = 'Mark Hellewell',
    author_email = 'mark.hellewell@commoncode.com.au',
    url = 'https://github.com/commoncode/platforms',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
        # 'entropy', # TODO: do the package location thing?
    ]
)
