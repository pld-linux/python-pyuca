#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module		pyuca
%define 	egg_name	pyuca
%define		pypi_name	pyuca
Summary:	A Python implementation of the Unicode Collation Algorithm
Name:		python-%{module}
Version:	1.1.2
Release:	6
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	083a414b2a81a9cd6e7f3d83443820f4
URL:		https://github.com/jtauber/pyuca
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python implementation of the Unicode Collation Algorithm.

%package -n python3-%{pypi_name}
Summary:	A Python implementation of the Unicode Collation Algorithm
Group:		Libraries/Python

%description -n python3-%{pypi_name}
A Python implementation of the Unicode Collation Algorithm.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
%{__rm} -r %{module}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc
%{py_sitescriptdir}/%{pypi_name}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc
%{py3_sitescriptdir}/%{pypi_name}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
