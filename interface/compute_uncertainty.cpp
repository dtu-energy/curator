#include "compute_uncertainty.h"
#include "atom.h"
#include "error.h"
#include "force.h"
#include "modify.h"
#include "pair_curator.h"
#include "update.h"
#include <cstring>

using namespace LAMMPS_NS;

ComputeUncertainty::ComputeUncertainty(LAMMPS *lmp, int narg, char **arg)
  : Compute(lmp, narg, arg) {
  if (narg != 4)
    error->all(FLERR, "Illegal compute uncertainty command");

  uncertainty_name = std::string(arg[3]);

  scalar_flag = 1;
  extscalar = 0;
  
  debug_mode = 0;

  // initialize pair and uncertainty pointer
  pair_ptr = NULL;
  if(const char* env_p = std::getenv("CURATOR_DEBUG")){
    debug_mode = 1;
  }
}

void ComputeUncertainty::init() {
  // Ensure pair style is properly initialized
  pair_ptr = force->pair;
  if (pair_ptr == NULL)
    error->all(FLERR, "Compute uncertainty requires a pair style to be defined");

  // Check if the pair style is PairCurator
  pair_curator = dynamic_cast<PairCurator *>(pair_ptr);
  if (pair_curator == NULL)
    error->all(FLERR, "Compute uncertainty can only be used with pair style 'curator'");
}

double ComputeUncertainty::compute_scalar() {
  invoked_scalar = update->ntimestep;
  scalar = pair_curator->get_uncertainty(uncertainty_name);
  if (debug_mode) {
    std::cout << "Key: " << uncertainty_name << ", Value: " << scalar << std::endl;
    std::cout << "Invoked Scalar: " << invoked_scalar << std::endl;
  }
  return scalar;
}

double ComputeUncertainty::memory_usage() {
  double bytes = sizeof(double);
  return bytes;
}