%global packname  CHNOSZ
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}
Summary:          Thermodynamic Calculations and Diagrams for Geochemistry

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
An integrated set of tools for thermodynamic calculations in aqueous
geochemistry and geobiochemistry. Functions are provided for writing
balanced reactions to form species from user-selected basis species and
for calculating the standard molal properties of species and reactions,
including the standard Gibbs energy and equilibrium constant. Calculations
of the non-equilibrium chemical affinity and equilibrium chemical activity
of species can be portrayed on diagrams as a function of temperature,
pressure, or activity of basis species; in two dimensions, this gives a
maximum affinity or predominance diagram. The diagrams have formatted
chemical formulas and axis labels, and water stability limits can be added
to Eh-pH, oxygen fugacity- temperature, and other diagrams with a redox
variable. The package has been developed to handle common calculations in
aqueous geochemistry, such as solubility due to complexation of metal
ions, mineral buffers of redox or pH, and changing the basis species
across a diagram ("mosaic diagrams"). CHNOSZ also has unique capabilities
for comparing the compositional and thermodynamic properties of different
proteins.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CHECKLIST
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/ONEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs