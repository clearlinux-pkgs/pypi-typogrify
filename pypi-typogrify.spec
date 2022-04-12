#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-typogrify
Version  : 2.0.7
Release  : 2
URL      : https://files.pythonhosted.org/packages/8a/bf/64959d6187d42472acb846bcf462347c9124952c05bd57e5769d5f28f9a6/typogrify-2.0.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/8a/bf/64959d6187d42472acb846bcf462347c9124952c05bd57e5769d5f28f9a6/typogrify-2.0.7.tar.gz
Summary  : Filters to enhance web typography, including support for Django & Jinja templates
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-typogrify-license = %{version}-%{release}
Requires: pypi-typogrify-python = %{version}-%{release}
Requires: pypi-typogrify-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(smartypants)

%description
transformations to plain text in order to yield typographically-improved HTML.
        While often used in conjunction with Jinja_ and Django_ template systems, the
        filters can be used in any environment.

%package license
Summary: license components for the pypi-typogrify package.
Group: Default

%description license
license components for the pypi-typogrify package.


%package python
Summary: python components for the pypi-typogrify package.
Group: Default
Requires: pypi-typogrify-python3 = %{version}-%{release}

%description python
python components for the pypi-typogrify package.


%package python3
Summary: python3 components for the pypi-typogrify package.
Group: Default
Requires: python3-core
Provides: pypi(typogrify)
Requires: pypi(smartypants)

%description python3
python3 components for the pypi-typogrify package.


%prep
%setup -q -n typogrify-2.0.7
cd %{_builddir}/typogrify-2.0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649789469
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-typogrify
cp %{_builddir}/typogrify-2.0.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-typogrify/36e5a9d5451ab860a39b5f6b5358db4d0840990f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-typogrify/36e5a9d5451ab860a39b5f6b5358db4d0840990f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
