Name:           gcadapter-oc-kmod
Version:        v1.4
Release:        1%{?dist}
Summary:        Kernel module for overclocking the Nintendo Wii U/Mayflash GameCube adapter.

License:        GPLv2
URL:            https://github.com/dhalucario/gcadapter-oc-kmod/
Source0:        https://github.com/dhalucario/gcadapter-oc-kmod/archive/refs/tags/%{version}.tar.gz

BuildRequires:  dkms
BuildRequires:  make
BuildRequires:  gcc
Requires:       dkms
Requires:       make
Requires:       gcc

%description

%prep
%setup -q

%install
ls
# tar -xvf %{version}.tar.gz
# install -Dm644 "${srcdir}"/dkms.conf "${pkgdir}"/usr/src/${pkgname}-${pkgver}/dkms.conf
# install -Dm644 "${srcdir}"/gcadapter-oc.conf "${pkgdir}"/usr/lib/modules-load.d/gcadapter-oc.conf
rm -rf $RPM_BUILD_ROOT

%files
%license add-license-file-here
%doc add-docs-here

%changelog
* Sat Oct 02 2021 Leon Grünewald <leon.gruenewald@kreativrudel.de>
- 
