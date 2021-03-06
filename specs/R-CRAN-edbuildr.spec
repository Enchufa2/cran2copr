%global packname  edbuildr
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}%{?buildtag}
Summary:          Automated School District Data Download and Processing

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 

%description
Import the 'EdBuild' master dataset of school district finance, student
demographics, and community economic indicators for every school district
in the United States. The master dataset is built from the US Census,
Annual Survey of School System Finances (F33) and joins data from the
National Center for Education Statistics, Common Core of Data; the US
Census, Small Area Income and Poverty Estimates; and the US Census,
Education Demographic and Geographic Estimates. We apply 'EdBuild'
standard processing to the dataset and provide the option to select from
four different exclusion criteria - see the masterpull() help file for
more details. The master dataset is available for any school year from
2013 to 2018 or longitudinally for all years 2013-2018. School year is
identified by the end year. For example, the 2017-18 school year is 2018.
Additional functions in the package use 'EdBuild' master data to analyze
the difference between neighboring school districts and create formatted
excel tables of school district data. For full details about 'EdBuild'
data processing please see 'EdBuild' (2020) <http://data.edbuild.org>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
