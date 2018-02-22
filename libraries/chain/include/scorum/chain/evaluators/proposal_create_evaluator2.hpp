#pragma once

#include <scorum/protocol/scorum_operations.hpp>
//#include <scorum/chain/committee_factory.hpp>

#include <scorum/chain/evaluators/evaluator.hpp>

namespace scorum {
namespace chain {

class account_service_i;
class proposal_service_i;
class registration_committee_service_i;
class dynamic_global_property_service_i;

class data_service_factory_i;

class proposal_create_evaluator2 : public evaluator_impl<data_service_factory_i, proposal_create_evaluator2>
{
public:
    using operation_type = scorum::protocol::proposal_create_operation2;

    using change_quorum_operation = scorum::protocol::registration_committee_change_quorum_operation;

    proposal_create_evaluator2(data_service_factory_i& services);

    void do_apply(const operation_type& op);

    protocol::percent_type get_quorum(const change_quorum_operation& op) const;

private:
    account_service_i& _account_service;
    proposal_service_i& _proposal_service;
    registration_committee_service_i& _committee_service;
    dynamic_global_property_service_i& _property_service;
};

} // namespace chain
} // namespace scorum
