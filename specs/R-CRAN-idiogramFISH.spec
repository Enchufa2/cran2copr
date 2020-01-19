%global packname  idiogramFISH
%global packver   1.12.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.1
Release:          1%{?dist}
Summary:          Idiograms with Marks and Karyotype Indices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 

%description
Plot idiograms of several karyotypes having a set of data.frames for
chromosome data and optionally mark data. Supports micrometers and Mb.
Marks can have square or dot form, its legend (label) can be drawn inline
or to the right of karyotypes. It is possible to calculate chromosome
indices by Levan et al. (1964) <doi:10.1111/j.1601-5223.1964.tb01953.x>,
karyotype indices of Watanabe et al. (1999) <doi:10.1007/PL00013869> and
Romero-Zarco (1986) <doi:10.2307/1221906> and classify chromosomes by
morphology Guerra (1986) and Levan et al. (1964).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX