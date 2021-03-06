%global packname  edbuildmapr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}%{?buildtag}
Summary:          Download School District Geospatial Data, Perform SpatialAnalysis, and Create Formatted Exportable Maps

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tmap >= 3.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.9.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-tmap >= 3.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-sf >= 0.9.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-stringr 

%description
Import US Census Bureau, Education Demographic and Geographic Estimates
Program, Composite School District Boundaries Files for 2013-2018 with the
option to attach the 'EdBuild' master dataset of school district finance,
student demographics, and community economic indicators for every school
district in the United States. The master dataset is built from the US
Census, Annual Survey of School System Finances (F33) and joins data from
the National Center for Education Statistics, Common Core of Data; the US
Census, Small Area Income and Poverty Estimates; and the US Census,
Education Demographic and Geographic Estimates. Additional functions in
the package create a dataset of all pairs of school district neighbors as
either a dataframe or a shapefile and create formatted maps of selected
districts at the state or neighbor level, symbolized by a selected
variable in the 'EdBuild' master dataset. For full details about 'EdBuild'
data processing please see 'EdBuild' (2020) <https://data.edbuild.org/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
