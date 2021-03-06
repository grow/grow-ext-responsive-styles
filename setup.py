from setuptools import setup


setup(
    name='grow-ext-responsive-styles',
    version='1.0.0',
    zip_safe=False,
    license='MIT',
    author='Grow Authors',
    author_email='hello@grow.io',
    include_package_data=True,
    packages=[
        'responsive_styles',
    ],
    package_data={
        'responsive_styles': ['*.html'],
    },
)
