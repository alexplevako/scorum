file(GLOB_RECURSE HEADERS "${CMAKE_CURRENT_SOURCE_DIR}/*.hpp"
                          "plugins/tags/*.hpp")

set( SOURCES
    main.cpp
    block_tests.cpp
    chain_api_tests.cpp
    operation_tests.cpp
    fork_tests.cpp
    escrow_transfer_operation_tests.cpp
    account_data_service_tests.cpp
    witness_data_service_tests.cpp
    operation_time_tests.cpp
    merkle_root_tests.cpp
    rewards/active_sp_holders_reward_tests.cpp
    rewards/reward_service_tests.cpp
    rewards/vote_apply_tests.cpp
    rewards/comment_beneficiaries_apply_tests.cpp
    rewards/per_block_reward_distribution.cpp
    rewards/fifa_world_cup_2018_bounty_reward_fund_tests.cpp
    rewards/comment_cashout_from_scr_fund_tests.cpp
    rewards/comment_hierarchy_reward_tests.cpp
    rewards/witness_reward_in_sp_migration_tests.cpp
    rewards/statistic_tests.cpp
    rewards/legacy_virtual_op_tests.cpp
    registration/registration_check_common.cpp
    registration/committee_service_tests.cpp
    registration/committee_operations_tests.cpp
    registration/create_by_committee_evaluator_tests.cpp
    registration/registration_service_tests.cpp
    registration/registration_helpers.cpp
    registration/burning_bonus.cpp
    atomicswap/atomicswap_service_tests.cpp
    atomicswap/atomicswap_operations_tests.cpp
    budget/budget_check_common.cpp
    budget/budget_service_tests.cpp
    budget/budget_autoclose_tests.cpp
    budget/budget_starting_tests.cpp
    budget/adv_moderator_tests.cpp
    budget/api/advertising_api_tests.cpp
    budget/budget_security_tests.cpp
    budget/budget_winners_tests.cpp
    proposal/proposal_tests.cpp
    plugins/statistic/node_monitoring_tests.cpp
    plugins/statistic/statistic_tests.cpp
    plugins/statistic/account_statistic_tests.cpp
    plugins/tags/tags_tests.cpp
    plugins/tags/get_comments_tests.cpp
    plugins/tags/get_tags_by_category_tests.cpp
    plugins/tags/get_discussions_by_author_tests.cpp
    plugins/tags/get_discussions_by_discussion_query_tests.cpp
    plugins/tags/get_contents_tests.cpp
    plugins/tags/get_posts_comments_by_author_tests.cpp
    plugins/tags/get_parents_tests.cpp
    plugins/blockchain_history_tests.cpp
    plugins/blockinfo_tests.cpp
    plugins/database_api/account_api_tests.cpp
    genesis_db_tests.cpp
    withdraw_scorumpower/old_tests.cpp
    withdraw_scorumpower/withdraw_scorumpower_check_common.cpp
    withdraw_scorumpower/route_from_account_to_account_tests.cpp
    withdraw_scorumpower/route_from_account_to_dev_pool_tests.cpp
    withdraw_scorumpower/route_from_dev_pool_to_account_tests.cpp
    withdraw_scorumpower/route_from_dev_pool_to_dev_pool_tests.cpp
    withdraw_scorumpower/lock_tests.cpp
    account/account_service_tests.cpp
    hardfork_tests.cpp
)

add_executable(chain_tests
             ${SOURCES}
             ${HEADERS})
target_link_libraries(chain_tests
                      common_test
                      scorum_app
                      scorum_rewards_math
                      scorum_egenesis_none
                      scorum_account_statistics
                      scorum_blockchain_monitoring
                      scorum_blockchain_history
                      )
target_include_directories(chain_tests PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}")

SET( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DSRC_DIR=${CMAKE_CURRENT_SOURCE_DIR}" )

OPTION(SCORUM_CHAIN_TESTS_LOG_MESSAGES "Show logs for chain tests (ON or OFF)" OFF)

MESSAGE( STATUS "  SCORUM_CHAIN_TESTS_LOG_MESSAGES:    ${SCORUM_CHAIN_TESTS_LOG_MESSAGES}" )
if( SCORUM_CHAIN_TESTS_LOG_MESSAGES )
    SET( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DLOG_MESSAGES" )
    SET( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DLOG_MESSAGES" )
endif()

if(MSVC)
    set_source_files_properties(serialization_tests.cpp PROPERTIES COMPILE_FLAGS "/bigobj" )
endif(MSVC)
