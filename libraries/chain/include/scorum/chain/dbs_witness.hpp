#pragma once

#include <memory>

#include <scorum/chain/dbservice_common.hpp>

namespace scorum {
namespace chain {

class dbservice;

class dbs_witness
{
public:
    explicit dbs_witness(dbservice& db);

    typedef std::unique_ptr<dbs_witness> ptr;

public:
    // TODO

private:
    dbservice& _db;
};
}
}
