%global packname  optimos.prime
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Optimos Prime Helps Calculate Autoecological Data for BiologicalSpecies

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-plotly 

%description
Calculates autoecological data (optima and tolerance ranges) of a
biological species given an environmental matrix. The package calculates
by weighted averaging, using the number of occurrences to adjust the
tolerance assigned to each taxon to estimate optima and tolerance range in
cases where taxa have unequal occurrences. See the detailed methodology by
Birks et al. (1990) <doi:10.1098/rstb.1990.0062>, and a case example by
Potapova and Charles (2003) <doi:10.1046/j.1365-2427.2003.01080.x>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
