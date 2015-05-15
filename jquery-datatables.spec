%define		plugin	datatables
Summary:	DataTables (table plug-in for jQuery)
Name:		jquery-%{plugin}
Version:	1.10.7
Release:	2
License:	GPL v2, BSD
Group:		Applications/WWW
Source0:	http://datatables.net/releases/DataTables-%{version}.zip
# Source0-md5:	d910448a806794a389d38678891cd779
Source1:	https://cdn.datatables.net/plug-ins/%{version}/i18n/Estonian.json
# Source1-md5:	eebbc70b2c466d438de450a4e5a340ff
Source2:	https://cdn.datatables.net/plug-ins/%{version}/i18n/Russian.json
# Source2-md5:	008b2f34327842d745bc826954e30978
Source3:	https://cdn.datatables.net/plug-ins/%{version}/i18n/Latvian.json
# Source3-md5:	ae7fb9599678aea84108918f31312c7e
Source4:	https://cdn.datatables.net/plug-ins/%{version}/i18n/Lithuanian.json
# Source4-md5:	3d340f69789a0c2a852656666ceb8437
URL:		http://www.datatables.net/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	jquery >= 1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
DataTables is a plug-in for the jQuery JavaScript library. It is a
highly flexible tool, based upon the foundations of progressive
enhancement, which will add advanced interaction controls to any HTML
table.

%prep
%setup -qn DataTables-%{version}

install -d i18n
cp -p %{SOURCE1} i18n
cp -p %{SOURCE2} i18n
cp -p %{SOURCE3} i18n
cp -p %{SOURCE4} i18n

%{__sed} -i -e 's,../images/,,' media/css/*.css
%{__rm} media/images/*.psd
%{__rm} media/images/*.ico

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a i18n $RPM_BUILD_ROOT%{_appdir}

cp -p media/js/jquery.dataTables.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p media/js/jquery.dataTables.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p media/css/jquery.dataTables.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css
ln -s %{plugin}-%{version}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

cp -a media/images/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md
%dir %{_appdir}
%{_appdir}/*.png
%{_appdir}/datatables*.css
%{_appdir}/datatables*.js
%dir %{_appdir}/i18n
%lang(et) %{_appdir}/i18n/Estonian.json
%lang(lt) %{_appdir}/i18n/Lithuanian.json
%lang(lv) %{_appdir}/i18n/Latvian.json
%lang(ru) %{_appdir}/i18n/Russian.json
