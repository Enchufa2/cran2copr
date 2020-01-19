%global packname  TR8
%global packver   0.9.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.20
Release:          1%{?dist}
Summary:          A Tool for Downloading Functional Traits Data for Plant Species

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-gWidgets 
BuildRequires:    R-CRAN-gWidgetstcltk 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-taxize 
Requires:         R-methods 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-gWidgets 
Requires:         R-CRAN-gWidgetstcltk 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-taxize 

%description
Plant ecologists often need to collect "traits" data about plant species
which are often scattered among various databases: TR8 contains a set of
tools which take care of automatically retrieving some of those functional
traits data for plant species from publicly available databases (Biolflor,
The Ecological Flora of the British Isles, LEDA traitbase, Ellenberg
values for Italian Flora, Mycorrhizal intensity databases, Catminat, BROT,
PLANTS, Jepson Flora Project). The TR8 name, inspired by "car plates"
jokes, was chosen since it both reminds of the main object of the package
and is extremely short to type.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX