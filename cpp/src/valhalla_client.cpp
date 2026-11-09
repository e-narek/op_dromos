#include "valhalla_client.hpp"

namespace op_dromos {

std::string ValhallaClient::status() const {
#ifdef OP_DROMOS_VALHALLA_AVAILABLE
  return "valhalla-linked";
#else
  return "valhalla-not-linked";
#endif
}

} // namespace op_dromos
