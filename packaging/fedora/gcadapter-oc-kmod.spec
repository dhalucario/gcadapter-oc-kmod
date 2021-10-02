
%global pkgname gcadapter-oc-kmod

Name:           %{pkgname}-dkms
Version:        v1.4
Release:        1%{?dist}
Summary:        Kernel module for overclocking the Nintendo Wii U/Mayflash GameCube adapter.

License:        GPLv2
URL:            https://github.com/dhalucario/gcadapter-oc-kmod/
Source0:        https://github.com/dhalucario/gcadapter-oc-kmod/archive/refs/tags/%{version}.tar.gz

Requires:       dkms
Requires:       make
Requires:       gcc
Provides:       %{pkgname}-dkms

%description

%post
%{_prefix}/lib/dkms/common.postinst %{pkgname} %{version}

%preun
if [ $1 -ne 1 ]; then
    dkms remove -m %{pkgname} -v %{version} --all --rpm_safe_upgrade || :
fi

%prep
%autosetup -c %{pkgname}-%{version}

%build
# Do nothing

%install
ls
cp %{pkgname}-%{version}/packaging/arch/dkms.conf %{pkgname}-%{version}/dkms.conf
sed -e "s/@PKGVER@/${version}/" -i "${pkgdir}"/usr/src/${pkgname}-${version}/dkms.conf

install -Dm664 %{pkgname}-%{version} "${RPM_BUILD_ROOT}%{_usrsrc}/"
rm -rf $RPM_BUILD_ROOT

%files
%license %{_usrsrc}/%{pkgname}-%{version}/LICENSE
%doc %{_usrsrc}/%{pkgname}-%{version}/README.md
%{_usrsrc}/%{pkgname}-%{version}

%changelog
* Sat Oct 02 2021 Leon Grünewald <leon.gruenewald@kreativrudel.de>
- Initial version
