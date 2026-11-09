#include <iostream>

#include "valhalla_client.hpp"

int main() {
  op_dromos::ValhallaClient client;
  std::cout << "route-engine:" << client.status() << '\n';
  return 0;
}
