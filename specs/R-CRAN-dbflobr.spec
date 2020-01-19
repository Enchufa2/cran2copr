%global packname  dbflobr
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Read and Write Files to SQLite Databases

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkr 
BuildRequires:    R-CRAN-flobr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-checkr 
Requires:         R-CRAN-flobr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 

%description
Reads and writes files to SQLite databases
<https://www.sqlite.org/index.html> as flobs (a flob is a blob that
preserves the file extension).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX