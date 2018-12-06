# https://github.com/cznic/sortutil
%global goipath github.com/cznic/sortutil
%global commit  4c7342852e65c2088c981288f2c5610d10b9f7f4

%gometa

Name:           golang-github-cznic-sortutil
Version:        0
Release:        0.8%{?dist}
Summary:        Supplemental utilities for Go's sort package
License:        BSD

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/cznic/mathutil)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS AUTHORS README


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20150617git4c73428
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.7.20150617git4c73428
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.20150617git4c73428
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git4c73428
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git4c73428
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git4c73428
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git4c73428
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.git4c73428
- First package for Fedora

