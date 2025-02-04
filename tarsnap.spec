#global commit  4db3705fa3ce0b0d45244a51acf78f2504988400
#global date 20170417
#global shortcommit0 #(c=#{commit}; echo ${c:0:7})

Name:           tarsnap
Version:        1.0.40
Release:        6%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:        Online encrypted backup service (client)

Group:          Applications/Archiving
# The following files are BSD licensed:
#  - libarchive/*
#  - lib/crypto/crypto_aesctr.*
#  - lib/crypto/crypto_scrypt.*
#  - lib/crypto/sha256.*
#  - lib/util/memlimit.*
#  - lib/util/readpass.*
#  - lib/util/sysendian.h
#  - lib/scryptenc/*
#  - tar/config_freebsd.h
#  - tar/siginfo.c
#  - tar/subst.c
# Portions of the following files are BSD licensed
# (the original BSD licensed code is in libarchive):
#  - tar/bsdtar*
#  - tar/cmdline.c
#  - tar/matching.c
#  - tar/read.c
#  - tar/tree.*
#  - tar/util.c
#  - tar/write.c
# The following file is in the public domain:
#  - tar/getdate.c
License:        Tarsnap License and BSD and Public Domain
URL:            https://www.tarsnap.com/
Source0:        https://github.com/Tarsnap/tarsnap/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  libattr-devel
BuildRequires:  automake

Provides:       bundled(libarchive) = 2.7.0

%description
Tarsnap is an online encrypted backup service.  It presents a tar-like
command-line interface, but stores data online rather than locally;
using ideas taken from the author's FreeBSD Update and Portsnap
utilities, it maximizes performance by recognizing duplicate data and
only storing it once, and cryptographically encrypts and signs archives
using locally-held keys in order to guarantee that nobody without access
to the key file (including the author) can read or modify archives.

%package bash-completion
Summary: Bash completion support for %{name}
BuildArch: noarch
Requires: bash
%description bash-completion
Bash completion support for the %{name}'s utilities.

%prep
%setup -q -n %{name}-%{version}
autoreconf -fiv

%build
%configure --disable-silent-rules \
 --with-bz2lib --with-lzmadec \
 --enable-largefile --enable-acl --disable-xattr \
 --with-lzma --with-bash-completion-dir=%{_sysconfdir}/bash_completion.d
%make_build


%install
%make_install

%files
%license COPYING
%config %{_sysconfdir}/tarsnap.conf.sample
%{_bindir}/tarsnap*
%{_mandir}/man*/tarsnap*

%files bash-completion
%license COPYING
%dir %{_sysconfdir}/bash_completion.d
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}-keygen
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}-recrypt
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}-keyregen
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}-keymgmt

%changelog
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sat Feb 26 2022 Sérgio Basto <sergio@serjux.com> - 1.0.40-1
- Update tarsnap to 1.0.40

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.39-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.39-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.39-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.39-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.39-4
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 18 2018 Sérgio Basto <sergio@serjux.com> - 1.0.39-1
- Update to 1.0.39 (#4792)

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.38-0.2.20170417git4db3705
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.38-0.1.20170417git4db3705
- Update to git snapshot to fix OpenSSL-1.1 compatibility

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.0.36.1-1
- Update to 1.0.36
- Spec cleaning
- Use %%license
- Made a bash_completion sub-package

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.32-2
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jun 24 2012 Ricky Zhou <ricky@fedoraproject.org> - 1.0.32-1
- Upstream released a new version.

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Ricky Zhou <ricky@fedoraproject.org> - 1.0.31-1
- Upstream released a new version.

* Thu Aug 25 2011 Ricky Zhou <ricky@fedoraproject.org> - 1.0.30-1
- Upstream released a new version.

* Tue Feb 08 2011 Ricky Zhou <ricky@fedoraproject.org> - 1.0.29-1
- Upstream released a new version.

* Tue Jan 18 2011 Ricky Zhou <ricky@fedoraproject.org> - 1.0.28-1
- Upstream released a new version.
- Fixes critical security bug in data encryption code.

* Sat Dec 04 2010 Ricky Zhou <ricky@fedoraproject.org> - 1.0.27-1
- Initial package.
