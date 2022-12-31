# pdf_summary

This code summarizes a PDF file. 

The code requires an API key from openai, which is stored in an `.env` file

The model uses the `"text-davinci-003"` engine, but a different engine can be used. 

Default is to return summaries suitable for a college professor, but this can be altered by changing the `type` parameter in the call to `summarize_page`.

When run from the command line, the code will output a summary of the PDF file, with each page summarized on its own line.

Here are the raw results generated using this code against the included `test_file.pdf`:

> python summarize.py test_file.pdf

```
{0: ' This paper presents a novel theoretical framework for the study of individual tree sap flow that incorporates both spatial and temporal variability in sap velocities. Experiments were conducted on sugar maples and dwarf apple trees to confirm the hypothesis that the characteristic distribution of sap velocity is relatively uniform both within individual trees and between trees of the same species. This method offers the potential to improve the sampling strategies used to estimate whole-tree transpiration and to upscale water use of individual trees to larger scales.',
 1: ' Recent methods of extrapolating radial velocity observations to estimate whole-tree sap flow have limitations. A new method is proposed which addresses these shortcomings and allows for sap flow to be generalized across different individuals or species, and to isolate the component of sap flow governed by the radial variation in hydraulic architecture.',
 2: ' We have developed a method for determining the instantaneous sap velocity at any point in the radial profile of a tree by defining the product of a time-invariant sap velocity distribution and a new time-varying term, stem conductance. This method allows us to scale up short-term estimates of sap flux in individual trees to longer time scales and trees of varying sizes.',
 3: ' It is possible to determine the instantaneous total sap flow of an individual tree from a single observation of sap velocity at a single depth within the xylem. This requires prior knowledge of the characteristic sap velocity profile and can be used to compare stem conductance between individual trees of different sizes or even between different species.',
 4: ' Seventeen sugar maple trees were selected along a south-facing topographic transect, and sap flow velocity was estimated using the compensation heat pulse technique. The parameters of the radial sap velocity profile were estimated using the least-square method. The results were compared to past empirical estimates of radial sap velocity profiles.',
 5: ' Results from the study showed that the Beta distribution function yielded coefficients of determination greater than 0.9 for both apple trees and sugar maples. The environmental conditions during the field experiments were similar, and the parameters a, b, and rs were observed in Acer saccharum during a 3-week field observation period. The estimated sap flux was strongly linearly correlated as expected.',
 6: ' The atmospheric VPD in a mixed forest stand at the Morgan Monroe State Forest facility was never greater than 2.5 kPa during the observation period. Soil water availability showed a marked decline beginning at the end of August, with volumetric water content ranging between 20% and 40%. There was also a large spatial variability in volumetric water content, ranging from 10% at the top of the hillslope to 30% at the bottom. Radial profiles in sap velocities were obtained over a wide range of environmental conditions and tree size, with the average values of a and b across all profiles being 5.3 and 2.0 for sugar maples and 4.2 and 2.8 for apple trees, respectively.',
 7: ' There is a strong linear correlation between sap flow and stem conductance, and the difference between sap flow estimates based on maximum likelihood estimates of all three parameters (a, b, and cs) and sap flow estimates based only on varying cs is minimal. The majority of the trees show differences less than 10%, with the exception of one sugar maple tree that resulted in about 40% greater flow. A power function was fit on the entire dataset, assuming that the error is 0 when the relative depth of the probe is 1.',
 8: ' The Hs, Zs, and Za methods for extrapolating observations across the active xylem using basic algebraic rules are not as accurate as the Gaussian method of describing sap velocity profiles developed by Ford et al. (2004). The Beta distribution function approach yields higher correlation coefficients and better describes the radial profile of sap velocities in both small and large diameter trees.',
 9: ' We have developed a theoretical framework for studying individual tree sap flow that incorporates both spatial and temporal variability. We used a Beta distribution to describe the characteristic radial profile of sap velocities, which is likely linked to the species-specific anatomical and structural properties of the conducting xylem. Our method attempts to decouple variability in sap velocity into two separate components and provides a direct mechanism for investigating how stem conductance is governed by variation in environmental conditions. Experimental evidence confirms the utility of our approach in the case of a population of sugar maples and apple trees, despite the fact that observations were drawn from a wide range of tree sizes.',
 10: ' This article reviews the literature on the use of sap flow measurements to estimate water use in trees, discussing the various techniques used, sources of error, and environmental drivers of spatial variation in whole-tree transpiration.'}
 ```
