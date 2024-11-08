# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: citadel_gcmessages_server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_pb2 as steammessages__pb2
import gcsdk_gcmessages_pb2 as gcsdk__gcmessages__pb2
import citadel_gcmessages_common_pb2 as citadel__gcmessages__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63itadel_gcmessages_server.proto\x1a\x13steammessages.proto\x1a\x16gcsdk_gcmessages.proto\x1a\x1f\x63itadel_gcmessages_common.proto\"\x8b\x05\n\x1b\x43MsgServerCrashSentinelFile\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x17\n\x0fserver_steam_id\x18\x02 \x01(\x06\x12\x1d\n\x15server_public_ip_addr\x18\x03 \x01(\x07\x12\x13\n\x0bserver_port\x18\x04 \x01(\r\x12\x16\n\x0eserver_cluster\x18\x05 \x01(\r\x12\x0b\n\x03pid\x18\x06 \x01(\r\x12\x12\n\nsaved_time\x18\x07 \x01(\r\x12\x16\n\x0eserver_version\x18\x08 \x01(\r\x12\x38\n\tgame_info\x18\t \x01(\x0b\x32%.CMsgServerCrashSentinelFile.GameInfo\x12\x1e\n\x16server_private_ip_addr\x18\n \x01(\r\x12\x13\n\x0binstance_id\x18\x0b \x01(\r\x1a-\n\x06Player\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x0f\n\x07hero_id\x18\x02 \x01(\r\x1a\x9e\x02\n\x08GameInfo\x12\x10\n\x08match_id\x18\x01 \x01(\x04\x12\x10\n\x08lobby_id\x18\x02 \x01(\x06\x12\x14\n\x0cserver_state\x18\x03 \x01(\r\x12\x34\n\x07players\x18\x05 \x03(\x0b\x32#.CMsgServerCrashSentinelFile.Player\x12\x43\n\nmatch_mode\x18\x06 \x01(\x0e\x32\x12.ECitadelMatchMode:\x1bk_ECitadelMatchMode_Invalid\x12@\n\tgame_mode\x18\x07 \x01(\x0e\x32\x11.ECitadelGameMode:\x1ak_ECitadelGameMode_Invalid\x12\x1b\n\x13was_server_shutdown\x18\x08 \x01(\x08\"\xb1\x01\n\x1a\x43ServerLobbyData_PlayerMMR\x12\x33\n\x07players\x18\x01 \x03(\x0b\x32\".CServerLobbyData_PlayerMMR.Player\x1a^\n\x06Player\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x12\n\nplayer_mmr\x18\x02 \x01(\r\x12\x1a\n\x12player_uncertainty\x18\x03 \x01(\r\x12\x10\n\x08hero_mmr\x18\x04 \x01(\r\"\x9c\x01\n\x1b\x43ServerLobbyData_PlayerInfo\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12,\n\raccount_stats\x18\x02 \x03(\x0b\x32\x15.CMsgAccountHeroStats\x12\x11\n\tmmr_level\x18\x04 \x01(\r\x12(\n\tbook_info\x18\x05 \x03(\x0b\x32\x15.CMsgAccountBookStats\"\x9c\x01\n CServerLobbyData_PostMatchSurvey\x12?\n\x07surveys\x18\x01 \x03(\x0b\x32..CServerLobbyData_PostMatchSurvey.PlayerSurvey\x1a\x37\n\x0cPlayerSurvey\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x13\n\x0bquestion_id\x18\x02 \x01(\r\"3\n\x19\x43ServerLobbyData_AutoTest\x12\x16\n\x0emax_duration_s\x18\x02 \x01(\r\"\x81\x01\n\x1c\x43SOCitadelServerDynamicLobby\x12\x10\n\x08lobby_id\x18\x01 \x01(\x04\x12\x1c\n\x10left_account_ids\x18\x02 \x03(\rB\x02\x10\x01\x12\x18\n\x10\x62roadcast_active\x18\x03 \x01(\x08\x12\x17\n\x0fspectator_count\x18\x04 \x01(\r\"\xdb\t\n\x1b\x43SOCitadelServerStaticLobby\x12\'\n\x0e\x65xtra_messages\x18\x01 \x03(\x0b\x32\x0f.CExtraMsgBlock\x12\x17\n\x0fserver_steam_id\x18\x02 \x01(\x06\x12\x10\n\x08lobby_id\x18\x03 \x01(\x04\x12\x13\n\x0breplay_salt\x18\x04 \x01(\x07\x12\x12\n\nlevel_name\x18\x05 \x01(\t\x12\x34\n\x07members\x18\x06 \x03(\x0b\x32#.CSOCitadelServerStaticLobby.Member\x12>\n\x0c\x64\x65v_settings\x18\x07 \x01(\x0b\x32(.CSOCitadelServerStaticLobby.DevSettings\x12\x1a\n\x12gc_provided_heroes\x18\x08 \x01(\x08\x12L\n\x0e\x62ot_difficulty\x18\t \x01(\x0e\x32\x16.ECitadelBotDifficulty:\x1ck_ECitadelBotDifficulty_None\x12\x15\n\rmetadata_salt\x18\n \x01(\x07\x12\x18\n\x10match_start_time\x18\x0b \x01(\r\x12#\n\x1b\x65xperimental_gameplay_state\x18\x0f \x01(\r\x12\x42\n\x0bregion_mode\x18\x10 \x01(\x0e\x32\x13.ECitadelRegionMode:\x18k_ECitadelRegionMode_ROW\x12\x15\n\rbroadcast_url\x18\x11 \x01(\t\x12\x17\n\x0fnew_player_pool\x18\x12 \x01(\x08\x12\x14\n\x0clow_pri_pool\x18\x13 \x01(\x08\x12\x1c\n\x14is_restricted_access\x18\x14 \x01(\x08\x12\x16\n\x0e\x63heats_enabled\x18\x15 \x01(\x08\x12 \n\x18\x64uplicate_heroes_enabled\x18\x16 \x01(\x08\x12#\n\x1bis_high_skill_range_parties\x18\x17 \x01(\x08\x12#\n\x1b\x65xperimental_heroes_enabled\x18\x18 \x01(\x08\x1a\x90\x03\n\x06Member\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x14\n\x0cpersona_name\x18\x02 \x01(\t\x12;\n\x04team\x18\x03 \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x12\x13\n\x0bplayer_slot\x18\x04 \x01(\r\x12\x0f\n\x07hero_id\x18\x05 \x01(\r\x12\x13\n\x0bparty_index\x18\x06 \x01(\r\x12\x32\n\x08platform\x18\x07 \x01(\x0e\x32\x0c.EGCPlatform:\x12k_eGCPlatform_None\x12\x39\n\taward_ids\x18\x08 \x03(\x0e\x32&.CSOCitadelServerStaticLobby.EAwardIDs\x12\x1b\n\x13is_comms_restricted\x18\t \x01(\x08\x12\x0f\n\x07lane_id\x18\n \x01(\r\x12\x1a\n\x12ranked_badge_level\x18\x0b \x01(\r\x12+\n\x0fgc_account_data\x18\r \x01(\x0b\x32\x12.CMsgGCAccountData\x1a%\n\x0b\x44\x65vSettings\x12\x16\n\x0e\x63onsole_string\x18\x01 \x01(\t\"#\n\tEAwardIDs\x12\x16\n\x12k_eAward_KingPanda\x10\x01\"\xe3\x07\n%CMsgServerSignoutData_ServerPerfStats\x12\x19\n\x11peak_memory_bytes\x18\x01 \x01(\x04\x12\x18\n\x10\x65nd_memory_bytes\x18\x02 \x01(\x04\x12\x1e\n\x16\x66rame_time_max_micro_s\x18\x03 \x01(\r\x12\x1d\n\x15\x66rame_time_95_micro_s\x18\x04 \x01(\r\x12\x1e\n\x16\x66rame_time_avg_micro_s\x18\x05 \x01(\r\x12\"\n\x1a\x66rame_idle_time_95_micro_s\x18\x06 \x01(\r\x12#\n\x1b\x66rame_idle_time_avg_micro_s\x18\x07 \x01(\r\x12\x1d\n\x15\x66rame_time_80_micro_s\x18\x08 \x01(\r\x12\x1d\n\x15\x66rame_time_99_micro_s\x18\t \x01(\r\x12M\n\x0cperf_samples\x18\n \x01(\x0b\x32\x37.CMsgServerSignoutData_ServerPerfStats.MatchPerfSamples\x1aH\n\x0b\x46rameCounts\x12\x12\n\nnum_frames\x18\x01 \x01(\r\x12\x13\n\x0blongest_run\x18\x02 \x01(\r\x12\x10\n\x08num_runs\x18\x03 \x01(\r\x1a\xf2\x02\n\nPerfSample\x12\x13\n\x0bgame_time_s\x18\x01 \x01(\r\x12\x11\n\tavg_frame\x18\x02 \x01(\x02\x12\x10\n\x08\x61vg_idle\x18\x03 \x01(\x02\x12\x14\n\x0ctotal_frames\x18\x04 \x01(\r\x12M\n\x11performant_frames\x18\x05 \x01(\x0b\x32\x32.CMsgServerSignoutData_ServerPerfStats.FrameCounts\x12G\n\x0blong_frames\x18\x06 \x01(\x0b\x32\x32.CMsgServerSignoutData_ServerPerfStats.FrameCounts\x12K\n\x0flow_idle_frames\x18\x07 \x01(\x0b\x32\x32.CMsgServerSignoutData_ServerPerfStats.FrameCounts\x12\x14\n\x0cmemory_bytes\x18\x08 \x01(\x04\x12\x19\n\x11peak_memory_bytes\x18\t \x01(\x04\x1a\x90\x01\n\x10MatchPerfSamples\x12\x1c\n\x14long_frame_threshold\x18\x01 \x01(\x02\x12\x1a\n\x12low_idle_threshold\x18\x02 \x01(\x02\x12\x42\n\x07samples\x18\x03 \x03(\x0b\x32\x31.CMsgServerSignoutData_ServerPerfStats.PerfSample\"\x81\x02\n\x1d\x43MsgServerToGCUpdateMatchInfo\x12\x10\n\x08lobby_id\x18\x01 \x01(\x04\x12\x14\n\x0ckills_team_0\x18\x03 \x01(\r\x12\x14\n\x0ckills_team_1\x18\x04 \x01(\r\x12\x18\n\x10net_worth_team_0\x18\x05 \x01(\r\x12\x18\n\x10net_worth_team_1\x18\x06 \x01(\r\x12\x12\n\nspectators\x18\x07 \x01(\r\x12\x1c\n\x14open_spectator_slots\x18\x08 \x01(\r\x12\x1d\n\x15objectives_mask_team0\x18\t \x01(\x04\x12\x1d\n\x15objectives_mask_team1\x18\n \x01(\x04\"\xb0\x01\n$CMsgServerToGCMatchSignoutPermission\x12\x15\n\rsignout_start\x18\x01 \x01(\r\x12\x1a\n\x12permission_request\x18\x02 \x01(\r\x12\x10\n\x08match_id\x18\x03 \x01(\x04\x12\x43\n\nmatch_mode\x18\x04 \x01(\x0e\x32\x12.ECitadelMatchMode:\x1bk_ECitadelMatchMode_Invalid\"\x89\x01\n,CMsgServerToGCMatchSignoutPermissionResponse\x12\x14\n\x0c\x63\x61n_sign_out\x18\x01 \x01(\x08\x12\x14\n\x0cretry_time_s\x18\x02 \x01(\r\x12-\n\x0erequested_data\x18\x03 \x03(\x0e\x32\x15.EGCServerSignoutData\"\xca\x02\n$CMsgServerSignoutData_Disconnections\x12T\n\x0e\x64isconnections\x18\x01 \x03(\x0b\x32<.CMsgServerSignoutData_Disconnections.CMsgMatchDisconnection\x1a\xcb\x01\n\x16\x43MsgMatchDisconnection\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x17\n\x0f\x64isconnect_time\x18\x02 \x01(\r\x12\x18\n\x10\x63onnection_state\x18\x03 \x01(\r\x12\x13\n\x0breason_code\x18\x04 \x01(\r\x12\x17\n\x0freconnect_delay\x18\x05 \x01(\r\x12\x1d\n\x15match_disconnect_time\x18\x06 \x01(\r\x12\x1d\n\x15match_reconnect_delay\x18\x07 \x01(\r\"\xb6\x0e\n#CMsgServerSignoutData_DetailedStats\x12\x41\n\x0cplayer_stats\x18\x01 \x03(\x0b\x32+.CMsgServerSignoutData_DetailedStats.Player\x12\x42\n\nobjectives\x18\x02 \x03(\x0b\x32..CMsgServerSignoutData_DetailedStats.Objective\x12>\n\x08mid_boss\x18\x03 \x03(\x0b\x32,.CMsgServerSignoutData_DetailedStats.MidBoss\x1a+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x1a\xc4\x07\n\nTimeSample\x12\x14\n\x0cmatch_time_s\x18\x01 \x01(\r\x12\x44\n\x05stats\x18\x02 \x01(\x0b\x32\x35.CMsgServerSignoutData_DetailedStats.TimeSample.Stats\x12M\n\ngold_stats\x18\x04 \x01(\x0b\x32\x39.CMsgServerSignoutData_DetailedStats.TimeSample.GoldStats\x1a\xa4\x04\n\x05Stats\x12\x11\n\tnet_worth\x18\x01 \x01(\r\x12\r\n\x05kills\x18\x02 \x01(\r\x12\x0e\n\x06\x64\x65\x61ths\x18\x03 \x01(\r\x12\x0f\n\x07\x61ssists\x18\x04 \x01(\r\x12\x17\n\x0fpossible_creeps\x18\x05 \x01(\r\x12\x13\n\x0b\x63reep_kills\x18\x06 \x01(\r\x12\x15\n\rneutral_kills\x18\x07 \x01(\r\x12\x14\n\x0c\x63reep_damage\x18\x08 \x01(\r\x12\x16\n\x0eneutral_damage\x18\t \x01(\r\x12\x13\n\x0b\x62oss_damage\x18\n \x01(\r\x12\x15\n\rplayer_damage\x18\x0b \x01(\r\x12\x0e\n\x06\x64\x65nies\x18\x0c \x01(\r\x12\x16\n\x0eplayer_healing\x18\r \x01(\r\x12\x16\n\x0e\x61\x62ility_points\x18\x0e \x01(\r\x12\x14\n\x0cself_healing\x18\x0f \x01(\r\x12\x1b\n\x13player_damage_taken\x18\x10 \x01(\r\x12\x12\n\nmax_health\x18\x11 \x01(\r\x12\x14\n\x0cweapon_power\x18\x12 \x01(\r\x12\x12\n\ntech_power\x18\x13 \x01(\r\x12\x11\n\tshots_hit\x18\x14 \x01(\r\x12\x14\n\x0cshots_missed\x18\x15 \x01(\r\x12\x17\n\x0f\x64\x61mage_absorbed\x18\x16 \x01(\r\x12\x1b\n\x13\x61\x62sorption_provided\x18\x17 \x01(\r\x12\x16\n\x0eheal_prevented\x18\x1a \x01(\r\x12\x11\n\theal_lost\x18\x1b \x01(\r\x1a\xe3\x01\n\tGoldStats\x12\x0e\n\x06player\x18\x01 \x01(\r\x12\x12\n\nplayer_orb\x18\x02 \x01(\r\x12\x16\n\x0elane_creep_orb\x18\x03 \x01(\r\x12\x19\n\x11neutral_creep_orb\x18\x04 \x01(\r\x12\x0c\n\x04\x62oss\x18\x05 \x01(\r\x12\x10\n\x08\x62oss_orb\x18\x06 \x01(\r\x12\x10\n\x08treasure\x18\x07 \x01(\r\x12\x0e\n\x06\x64\x65nied\x18\x08 \x01(\r\x12\x12\n\ndeath_loss\x18\t \x01(\r\x12\x12\n\nlane_creep\x18\n \x01(\r\x12\x15\n\rneutral_creep\x18\x0b \x01(\r\x1a\xbe\x02\n\tObjective\x12\x18\n\x10\x64\x65stroyed_time_s\x18\x02 \x01(\r\x12\x14\n\x0c\x63reep_damage\x18\x04 \x01(\r\x12\x1e\n\x16\x63reep_damage_mitigated\x18\x05 \x01(\r\x12\x15\n\rplayer_damage\x18\x06 \x01(\r\x12\x1f\n\x17player_damage_mitigated\x18\x07 \x01(\r\x12\x1b\n\x13\x66irst_damage_time_s\x18\x08 \x01(\r\x12O\n\x11team_objective_id\x18\t \x01(\x0e\x32\x16.ECitadelTeamObjective:\x1ck_eCitadelTeamObjective_Core\x12;\n\x04team\x18\n \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x1a\xac\x01\n\x07MidBoss\x12\x42\n\x0bteam_killed\x18\x01 \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x12\x43\n\x0cteam_claimed\x18\x02 \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x12\x18\n\x10\x64\x65stroyed_time_s\x18\x03 \x01(\r\x1a\x64\n\x06Player\x12\x13\n\x0bplayer_slot\x18\x01 \x01(\r\x12\x45\n\x0ctime_samples\x18\x03 \x03(\x0b\x32/.CMsgServerSignoutData_DetailedStats.TimeSample\"\xe2\x05\n\x1e\x43MsgServerSignoutData_PerfData\x12\x1a\n\x12\x61verage_frame_time\x18\x01 \x03(\x02\x12\x16\n\x0emax_frame_time\x18\x02 \x03(\x02\x12!\n\x19server_average_frame_time\x18\x03 \x01(\x02\x12\x1d\n\x15server_max_frame_time\x18\x04 \x01(\x02\x12\x1c\n\x14\x61verage_compute_time\x18\x05 \x03(\x02\x12\x18\n\x10max_compute_time\x18\x06 \x03(\x02\x12 \n\x18\x61verage_client_tick_time\x18\x07 \x03(\x02\x12\x1c\n\x14max_client_tick_time\x18\x08 \x03(\x02\x12$\n\x1c\x61verage_client_simulate_time\x18\t \x03(\x02\x12 \n\x18max_client_simulate_time\x18\n \x03(\x02\x12\x1b\n\x13\x61verage_output_time\x18\x0b \x03(\x02\x12\x17\n\x0fmax_output_time\x18\x0c \x03(\x02\x12\x33\n+average_wait_for_rendering_to_complete_time\x18\r \x03(\x02\x12/\n\'max_wait_for_rendering_to_complete_time\x18\x0e \x03(\x02\x12\x19\n\x11\x61verage_swap_time\x18\x0f \x03(\x02\x12\x15\n\rmax_swap_time\x18\x10 \x03(\x02\x12!\n\x19\x61verage_frame_update_time\x18\x11 \x03(\x02\x12\x1d\n\x15max_frame_update_time\x18\x12 \x03(\x02\x12\x19\n\x11\x61verage_idle_time\x18\x13 \x03(\x02\x12\x15\n\rmax_idle_time\x18\x14 \x03(\x02\x12%\n\x1d\x61verage_input_processing_time\x18\x15 \x03(\x02\x12!\n\x19max_input_processing_time\x18\x16 \x03(\x02\"\x8b\x02\n!CMsgServerSignoutData_BookRewards\x12J\n\x0f\x61\x63\x63ount_rewards\x18\x01 \x03(\x0b\x32\x31.CMsgServerSignoutData_BookRewards.AccountRewards\x1a\x30\n\nBookReward\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\r\x12\x11\n\txp_reward\x18\x02 \x01(\r\x1ah\n\x0e\x41\x63\x63ountRewards\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x42\n\x0b\x62ook_reward\x18\x02 \x01(\x0b\x32-.CMsgServerSignoutData_BookRewards.BookReward\"\xc8\x02\n(CMsgServerSignoutData_AccountStatChanges\x12M\n\raccount_stats\x18\x01 \x03(\x0b\x32\x36.CMsgServerSignoutData_AccountStatChanges.AccountStats\x1aj\n\x04Stat\x12\x0f\n\x07hero_id\x18\x01 \x01(\r\x12\x0f\n\x07stat_id\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\r\x12\x31\n\x05medal\x18\x04 \x01(\x0e\x32\x19.ECitadelAccountStatMedal:\x07k_eNone\x1a\x61\n\x0c\x41\x63\x63ountStats\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12=\n\x05stats\x18\x02 \x03(\x0b\x32..CMsgServerSignoutData_AccountStatChanges.Stat\"\xbc\x01\n CMsgServerSignoutData_PlayerChat\x12>\n\nchat_lines\x18\x01 \x03(\x0b\x32*.CMsgServerSignoutData_PlayerChat.ChatLine\x1aX\n\x08\x43hatLine\x12\x13\n\x0bplayer_slot\x18\x01 \x01(\r\x12\x11\n\tgame_time\x18\x02 \x01(\x02\x12\x11\n\tteam_only\x18\x03 \x01(\x08\x12\x11\n\tchat_line\x18\x04 \x01(\t\"\x94\x03\n&CMsgServerSignoutData_PenalizedPlayers\x12J\n\x11penalized_players\x18\x01 \x03(\x0b\x32/.CMsgServerSignoutData_PenalizedPlayers.Penalty\x1a\xa9\x01\n\x07Penalty\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12`\n\x06reason\x18\x02 \x01(\x0e\x32\x36.CMsgServerSignoutData_PenalizedPlayers.EPenaltyReason:\x18k_EPenaltyReason_Abandon\x12\x14\n\x0cmatch_time_s\x18\x03 \x01(\r\x12\x12\n\ntime_stamp\x18\x04 \x01(\r\"r\n\x0e\x45PenaltyReason\x12\x1c\n\x18k_EPenaltyReason_Abandon\x10\x00\x12(\n$k_EPenaltyReason_DisconnectedTooLong\x10\x01\x12\x18\n\x14k_EPenaltyReason_AFK\x10\x02\"\x87\x10\n\rCMsgMatchData\x12\x18\n\x10match_duration_s\x18\x01 \x01(\r\x12\x43\n\nend_reason\x18\x02 \x01(\x0e\x32\x19.CMsgMatchData.EEndReason:\x14k_EEndReason_TeamWin\x12\x43\n\x0cwinning_team\x18\x03 \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x12*\n\x07players\x18\x04 \x03(\x0b\x32\x19.CMsgMatchData.PlayerInfo\x12\x1e\n\x16objectives_mask_legacy\x18\x05 \x01(\r\x12\x16\n\x0eserver_version\x18\x06 \x01(\r\x12@\n\tgame_mode\x18\x07 \x01(\x0e\x32\x11.ECitadelGameMode:\x1ak_ECitadelGameMode_Invalid\x12\x43\n\nmatch_mode\x18\x08 \x01(\x0e\x32\x12.ECitadelMatchMode:\x1bk_ECitadelMatchMode_Invalid\x12\x1d\n\x15objectives_mask_team0\x18\t \x01(\x04\x12\x1d\n\x15objectives_mask_team1\x18\n \x01(\x04\x12\x16\n\x0ematch_end_time\x18\x0b \x01(\r\x12\x13\n\x0bstomp_score\x18\x0c \x01(\x02\x12\x17\n\x0fsafe_to_abandon\x18\r \x01(\x08\x12\x14\n\x0cteam_abandon\x18\x0e \x01(\x08\x12\x17\n\x0fnew_player_pool\x18\x0f \x01(\x08\x12\x14\n\x0clow_pri_pool\x18\x10 \x01(\x08\x1a\x85\x01\n\nPlayerItem\x12\x0f\n\x07item_id\x18\x01 \x01(\r\x12\x13\n\x0bgame_time_s\x18\x02 \x01(\r\x12\x12\n\nupgrade_id\x18\x03 \x01(\r\x12\x13\n\x0bsold_time_s\x18\x04 \x01(\r\x12\r\n\x05\x66lags\x18\x05 \x01(\r\x12\x19\n\x11imbued_ability_id\x18\x06 \x01(\r\x1a\xe8\x08\n\nPlayerInfo\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12;\n\x04team\x18\x02 \x01(\x0e\x32\x12.ECitadelLobbyTeam:\x19k_ECitadelLobbyTeam_Team0\x12\x13\n\x0bplayer_slot\x18\x03 \x01(\r\x12\x12\n\nplayer_mmr\x18\x05 \x01(\r\x12\x1a\n\x12player_uncertainty\x18\x06 \x01(\r\x12\x0f\n\x07hero_id\x18\x07 \x01(\r\x12\r\n\x05kills\x18\x08 \x01(\r\x12\x0e\n\x06\x64\x65\x61ths\x18\t \x01(\r\x12\x11\n\tnet_worth\x18\n \x01(\r\x12\x0f\n\x07\x61ssists\x18\x0b \x01(\r\x12\x10\n\x08hero_mmr\x18\x0c \x01(\r\x12(\n\x05items\x18\r \x03(\x0b\x32\x19.CMsgMatchData.PlayerItem\x12\x11\n\tgpm_10min\x18\x0e \x01(\r\x12\x11\n\tgpm_15min\x18\x0f \x01(\r\x12\x11\n\tgpm_20min\x18\x10 \x01(\r\x12\x11\n\tgpm_25min\x18\x11 \x01(\r\x12\x11\n\tgpm_30min\x18\x12 \x01(\r\x12\x11\n\tgpm_35min\x18\x13 \x01(\r\x12\x0f\n\x07gpm_end\x18\x14 \x01(\r\x12\x11\n\tlast_hits\x18\x15 \x01(\r\x12\x0e\n\x06\x64\x65nies\x18\x16 \x01(\r\x12\x16\n\x0e\x61\x62ility_points\x18\x17 \x01(\r\x12\r\n\x05level\x18\x18 \x01(\r\x12\x15\n\rassigned_lane\x18\x19 \x01(\r\x12\x13\n\x0bparty_index\x18\x1a \x01(\r\x12\x32\n\x08platform\x18\x1b \x01(\x0e\x32\x0c.EGCPlatform:\x12k_eGCPlatform_None\x12\x16\n\x0e\x61\x62ility_damage\x18\x1c \x01(\r\x12\x15\n\rbullet_damage\x18\x1d \x01(\r\x12\x18\n\x10hero_bullets_hit\x18\x1e \x01(\r\x12\x1d\n\x15hero_bullets_hit_crit\x18\x1f \x01(\r\x12\x16\n\x0eplayer_healing\x18  \x01(\r\x12\x1a\n\x12hero_bullets_fired\x18! \x01(\r\x12#\n\x1bhero_incoming_bullets_fired\x18\" \x01(\r\x12!\n\x19hero_incoming_bullets_hit\x18# \x01(\r\x12\"\n\x1ahero_incoming_bullets_crit\x18$ \x01(\r\x12\x13\n\x0btime_dead_s\x18% \x01(\r\x12\x1c\n\x14player_bullet_damage\x18& \x01(\r\x12\x1d\n\x15player_ability_damage\x18\' \x01(\r\x12\x1b\n\x13player_melee_damage\x18( \x01(\r\x12\x1c\n\x14\x61\x62\x61ndon_match_time_s\x18) \x01(\r\x12\x1a\n\x12\x61\x62\x61ndon_time_stamp\x18* \x01(\r\x12\x1d\n\x15trooper_kill_excluded\x18+ \x01(\r\x12 \n\x18hero_bullets_lucky_shots\x18, \x01(\r\x12\x15\n\rhero_build_id\x18- \x01(\r\"\xaa\x01\n\nEEndReason\x12\x18\n\x14k_EEndReason_TeamWin\x10\x00\x12\x1d\n\x19k_EEndReason_AllAbandoned\x10\x02\x12\x1e\n\x1ak_EEndReason_NetworkIssues\x10\x03\x12\x1c\n\x18k_EEndReason_MatchLength\x10\x04\x12%\n!k_EEndReason_PlayerNeverConnected\x10\x05\"\xbb\x01\n\x1a\x43MsgServerToGCMatchSignout\x12(\n\x0f\x61\x64\x64itional_data\x18\x01 \x03(\x0b\x32\x0f.CExtraMsgBlock\x12\x17\n\x0fsignout_attempt\x18\x02 \x01(\r\x12\x10\n\x08lobby_id\x18\x03 \x01(\x04\x12\x10\n\x08match_id\x18\x04 \x01(\x04\x12\x12\n\ncluster_id\x18\t \x01(\r\x12\"\n\nmatch_data\x18\n \x01(\x0b\x32\x0e.CMsgMatchData\"\xb1\x02\n\"CMsgServerToGCMatchSignoutResponse\x12[\n\x06result\x18\x01 \x01(\x0e\x32\x32.CMsgServerToGCMatchSignoutResponse.ESignoutResult:\x17k_ESignout_Failed_Retry\"\xad\x01\n\x0e\x45SignoutResult\x12\x1b\n\x17k_ESignout_Failed_Retry\x10\x01\x12\x1d\n\x19k_ESignout_Failed_NoRetry\x10\x02\x12\x1e\n\x1ak_ESignout_Failed_InFlight\x10\x03\x12\x16\n\x12k_ESignout_Success\x10\x04\x12\'\n#k_ESignout_Success_AlreadySignedOut\x10\x05\"\x1a\n\x18\x43MsgServerWelcomeCitadel\"0\n\x16\x43MsgServerToGCIdlePing\x12\x16\n\x0eserver_version\x18\x01 \x01(\r\"\x1b\n\x19\x43MsgGCToServerRequestPing\"2\n\x1e\x43MsgGCToServerAllocateForMatch\x12\x10\n\x08match_id\x18\x01 \x01(\x04\"9\n&CMsgGCToServerAllocateForMatchResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\xd2\x01\n\x1e\x43MsgServerToGCEnterMatchmaking\x12\x16\n\x0eserver_version\x18\x01 \x01(\r\x12\x12\n\nsearch_key\x18\x02 \x01(\t\x12\x11\n\tregion_id\x18\x03 \x01(\r\x12\x12\n\ncluster_id\x18\x04 \x01(\r\x12\x18\n\x10server_public_ip\x18\x05 \x01(\r\x12\x19\n\x11server_private_ip\x18\x06 \x01(\r\x12\x13\n\x0bserver_port\x18\x07 \x01(\r\x12\x13\n\x0bsdr_address\x18\t \x01(\x0c\"8\n$CMsgGCToServerCancelAllocateForMatch\x12\x10\n\x08match_id\x18\x01 \x01(\x04\"\x97\x01\n$CMsgServerToGCUpdateLobbyServerState\x12\x10\n\x08lobby_id\x18\x01 \x01(\x04\x12\x44\n\x0cserver_state\x18\x02 \x01(\x0e\x32\x12.ELobbyServerState:\x1ak_eLobbyServerState_Assign\x12\x17\n\x0fsafe_to_abandon\x18\x03 \x01(\x08\"\xbd\x05\n\x1a\x43MsgServerToGCAbandonMatch\x12\x17\n\x0fserver_steam_id\x18\x01 \x01(\x06\x12\x10\n\x08lobby_id\x18\x02 \x01(\x06\x12\x12\n\ncluster_id\x18\x03 \x01(\r\x12M\n\x0breason_code\x18\x04 \x01(\x0e\x32#.CMsgServerToGCAbandonMatch.EReason:\x13\x65Reason_ServerCrash\x12\x17\n\x0f\x61\x64\x64itional_data\x18\x05 \x01(\x04\x12\x10\n\x08match_id\x18\x06 \x01(\x04\x12\x33\n\x07players\x18\x08 \x03(\x0b\x32\".CMsgServerToGCAbandonMatch.Player\x12\x19\n\x11public_ip_address\x18\t \x01(\x07\x12\x0c\n\x04port\x18\n \x01(\r\x12\x16\n\x0eserver_version\x18\x0b \x01(\r\x12\x0b\n\x03pid\x18\x0c \x01(\r\x12\x13\n\x0binstance_id\x18\r \x01(\r\x12\x1a\n\x12private_ip_address\x18\x0e \x01(\r\x12\x43\n\nmatch_mode\x18\x0f \x01(\x0e\x32\x12.ECitadelMatchMode:\x1bk_ECitadelMatchMode_Invalid\x12@\n\tgame_mode\x18\x10 \x01(\x0e\x32\x11.ECitadelGameMode:\x1ak_ECitadelGameMode_Invalid\x12\x1b\n\x13was_server_shutdown\x18\x11 \x01(\x08\x1a\x46\n\x06Player\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x17\n\x0f\x61\x64\x64itional_data\x18\x02 \x01(\x04\x12\x0f\n\x07hero_id\x18\x03 \x01(\r\"F\n\x07\x45Reason\x12\x17\n\x13\x65Reason_ServerCrash\x10\x01\x12\"\n\x1e\x65Reason_ClientsFailedToConnect\x10\x02\"$\n\"CMsgServerToGCAbandonMatchResponse\"\x1e\n\x1c\x43MsgServerToGCTestConnection\"G\n$CMsgServerToGCTestConnectionResponse\x12\r\n\x05state\x18\x01 \x01(\r\x12\x10\n\x08lobby_id\x18\x02 \x01(\x04\"J\n\x1d\x43MsgGCToServerSetServerConVar\x12\x13\n\x0b\x63onvar_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63onvar_value\x18\x02 \x01(\t\"8\n%CMsgGCToServerSetServerConVarResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"_\n\x1a\x43MsgGCToServerAddSpectator\x12\x10\n\x08lobby_id\x18\x01 \x01(\x04\x12\x12\n\naccount_id\x18\x02 \x01(\r\x12\x1b\n\x13\x61\x63\x63ount_to_spectate\x18\x03 \x01(\r\"\xda\x01\n\"CMsgGCToServerAddSpectatorResponse\x12O\n\x06result\x18\x01 \x01(\x0e\x32-.CMsgGCToServerAddSpectatorResponse.EResponse:\x10k_eInternalError\x12\x1d\n\x15requesting_account_id\x18\x02 \x01(\r\"D\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x11\n\rk_eServerFull\x10\x02\"\x96\x01\n\x1b\x43MsgServerToGCReportCheater\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x10\n\x08match_id\x18\x02 \x01(\x04\x12\x10\n\x08lobby_id\x18\x03 \x01(\x06\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x18\n\x10record_data_only\x18\x05 \x01(\x08\x12\x15\n\rcheater_score\x18\x06 \x01(\x02\"6\n#CMsgServerToGCReportCheaterResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08*\x9a\x07\n\x18\x45GCCitadelServerMessages\x12+\n&k_EMsgServerToGCMatchSignoutPermission\x10\x9cN\x12\x33\n.k_EMsgServerToGCMatchSignoutPermissionResponse\x10\x9dN\x12!\n\x1ck_EMsgServerToGCMatchSignout\x10\x9eN\x12)\n$k_EMsgServerToGCMatchSignoutResponse\x10\x9fN\x12!\n\x1ck_EMsgGCToServerAddSpectator\x10\xa0N\x12)\n$k_EMsgGCToServerAddSpectatorResponse\x10\xa1N\x12\x1d\n\x18k_EMsgServerToGCIdlePing\x10\xa2N\x12 \n\x1bk_EMsgGCToServerRequestPing\x10\xa3N\x12%\n k_EMsgGCToServerAllocateForMatch\x10\xa5N\x12-\n(k_EMsgGCToServerAllocateForMatchResponse\x10\xa6N\x12%\n k_EMsgServerToGCEnterMatchmaking\x10\xa7N\x12+\n&k_EMsgGCToServerCancelAllocateForMatch\x10\xa8N\x12+\n&k_EMsgServerToGCUpdateLobbyServerState\x10\xa9N\x12!\n\x1ck_EMsgServerToGCAbandonMatch\x10\xaaN\x12)\n$k_EMsgServerToGCAbandonMatchResponse\x10\xabN\x12#\n\x1ek_EMsgServerToGCTestConnection\x10\xacN\x12+\n&k_EMsgServerToGCTestConnectionResponse\x10\xadN\x12$\n\x1fk_EMsgGCToServerSetServerConVar\x10\xb7N\x12,\n\'k_EMsgGCToServerSetServerConVarResponse\x10\xb8N\x12$\n\x1fk_EMsgServerToGCUpdateMatchInfo\x10\xb9N\x12\"\n\x1dk_EMsgServerToGCReportCheater\x10\xbaN\x12*\n%k_EMsgServerToGCReportCheaterResponse\x10\xbbN*\xa2\x01\n\x12\x45GCServerLobbyData\x12 \n\x1ck_EServerLobbyData_PlayerMMR\x10\x01\x12!\n\x1dk_EServerLobbyData_PlayerInfo\x10\x02\x12&\n\"k_EServerLobbyData_PostMatchSurvey\x10\x03\x12\x1f\n\x1bk_EServerLobbyData_AutoTest\x10\x04*\x80\x03\n\x14\x45GCServerSignoutData\x12\'\n#k_EServerSignoutData_Disconnections\x10\x02\x12+\n\'k_EServerSignoutData_AccountStatChanges\x10\x03\x12&\n\"k_EServerSignoutData_DetailedStats\x10\x04\x12(\n$k_EServerSignoutData_ServerPerfStats\x10\x05\x12!\n\x1dk_EServerSignoutData_PerfData\x10\x06\x12#\n\x1fk_EServerSignoutData_PlayerChat\x10\x07\x12$\n k_EServerSignoutData_BookRewards\x10\x08\x12)\n%k_EServerSignoutData_PenalizedPlayers\x10\t\x12\'\n#k_EServerSignoutData_ReportCheaters\x10\n')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'citadel_gcmessages_server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CSOCITADELSERVERDYNAMICLOBBY.fields_by_name['left_account_ids']._options = None
  _CSOCITADELSERVERDYNAMICLOBBY.fields_by_name['left_account_ids']._serialized_options = b'\020\001'
  _EGCCITADELSERVERMESSAGES._serialized_start=13103
  _EGCCITADELSERVERMESSAGES._serialized_end=14025
  _EGCSERVERLOBBYDATA._serialized_start=14028
  _EGCSERVERLOBBYDATA._serialized_end=14190
  _EGCSERVERSIGNOUTDATA._serialized_start=14193
  _EGCSERVERSIGNOUTDATA._serialized_end=14577
  _CMSGSERVERCRASHSENTINELFILE._serialized_start=114
  _CMSGSERVERCRASHSENTINELFILE._serialized_end=765
  _CMSGSERVERCRASHSENTINELFILE_PLAYER._serialized_start=431
  _CMSGSERVERCRASHSENTINELFILE_PLAYER._serialized_end=476
  _CMSGSERVERCRASHSENTINELFILE_GAMEINFO._serialized_start=479
  _CMSGSERVERCRASHSENTINELFILE_GAMEINFO._serialized_end=765
  _CSERVERLOBBYDATA_PLAYERMMR._serialized_start=768
  _CSERVERLOBBYDATA_PLAYERMMR._serialized_end=945
  _CSERVERLOBBYDATA_PLAYERMMR_PLAYER._serialized_start=851
  _CSERVERLOBBYDATA_PLAYERMMR_PLAYER._serialized_end=945
  _CSERVERLOBBYDATA_PLAYERINFO._serialized_start=948
  _CSERVERLOBBYDATA_PLAYERINFO._serialized_end=1104
  _CSERVERLOBBYDATA_POSTMATCHSURVEY._serialized_start=1107
  _CSERVERLOBBYDATA_POSTMATCHSURVEY._serialized_end=1263
  _CSERVERLOBBYDATA_POSTMATCHSURVEY_PLAYERSURVEY._serialized_start=1208
  _CSERVERLOBBYDATA_POSTMATCHSURVEY_PLAYERSURVEY._serialized_end=1263
  _CSERVERLOBBYDATA_AUTOTEST._serialized_start=1265
  _CSERVERLOBBYDATA_AUTOTEST._serialized_end=1316
  _CSOCITADELSERVERDYNAMICLOBBY._serialized_start=1319
  _CSOCITADELSERVERDYNAMICLOBBY._serialized_end=1448
  _CSOCITADELSERVERSTATICLOBBY._serialized_start=1451
  _CSOCITADELSERVERSTATICLOBBY._serialized_end=2694
  _CSOCITADELSERVERSTATICLOBBY_MEMBER._serialized_start=2218
  _CSOCITADELSERVERSTATICLOBBY_MEMBER._serialized_end=2618
  _CSOCITADELSERVERSTATICLOBBY_DEVSETTINGS._serialized_start=2620
  _CSOCITADELSERVERSTATICLOBBY_DEVSETTINGS._serialized_end=2657
  _CSOCITADELSERVERSTATICLOBBY_EAWARDIDS._serialized_start=2659
  _CSOCITADELSERVERSTATICLOBBY_EAWARDIDS._serialized_end=2694
  _CMSGSERVERSIGNOUTDATA_SERVERPERFSTATS._serialized_start=2697
  _CMSGSERVERSIGNOUTDATA_SERVERPERFSTATS._serialized_end=3692
  _CMSGSERVERSIGNOUTDATA_SERVERPERFSTATS_FRAMECOUNTS._serialized_start=3100
  _CMSGSERVERSIGNOUTDATA_SERVERPERFSTATS_FRAMECOUNTS._serialized_end=3172
  _CMSGSERVERSIGNOUTDATA_SERVERPERFSTATS_PERFSAMPLE._serialized_start=3175
  _CMSGSERVERSIGNOUTDATA_SERVERPERFSTATS_PERFSAMPLE._serialized_end=3545
  _CMSGSERVERSIGNOUTDATA_SERVERPERFSTATS_MATCHPERFSAMPLES._serialized_start=3548
  _CMSGSERVERSIGNOUTDATA_SERVERPERFSTATS_MATCHPERFSAMPLES._serialized_end=3692
  _CMSGSERVERTOGCUPDATEMATCHINFO._serialized_start=3695
  _CMSGSERVERTOGCUPDATEMATCHINFO._serialized_end=3952
  _CMSGSERVERTOGCMATCHSIGNOUTPERMISSION._serialized_start=3955
  _CMSGSERVERTOGCMATCHSIGNOUTPERMISSION._serialized_end=4131
  _CMSGSERVERTOGCMATCHSIGNOUTPERMISSIONRESPONSE._serialized_start=4134
  _CMSGSERVERTOGCMATCHSIGNOUTPERMISSIONRESPONSE._serialized_end=4271
  _CMSGSERVERSIGNOUTDATA_DISCONNECTIONS._serialized_start=4274
  _CMSGSERVERSIGNOUTDATA_DISCONNECTIONS._serialized_end=4604
  _CMSGSERVERSIGNOUTDATA_DISCONNECTIONS_CMSGMATCHDISCONNECTION._serialized_start=4401
  _CMSGSERVERSIGNOUTDATA_DISCONNECTIONS_CMSGMATCHDISCONNECTION._serialized_end=4604
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS._serialized_start=4607
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS._serialized_end=6453
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_POSITION._serialized_start=4845
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_POSITION._serialized_end=4888
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_TIMESAMPLE._serialized_start=4891
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_TIMESAMPLE._serialized_end=5855
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_TIMESAMPLE_STATS._serialized_start=5077
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_TIMESAMPLE_STATS._serialized_end=5625
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_TIMESAMPLE_GOLDSTATS._serialized_start=5628
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_TIMESAMPLE_GOLDSTATS._serialized_end=5855
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_OBJECTIVE._serialized_start=5858
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_OBJECTIVE._serialized_end=6176
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_MIDBOSS._serialized_start=6179
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_MIDBOSS._serialized_end=6351
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_PLAYER._serialized_start=6353
  _CMSGSERVERSIGNOUTDATA_DETAILEDSTATS_PLAYER._serialized_end=6453
  _CMSGSERVERSIGNOUTDATA_PERFDATA._serialized_start=6456
  _CMSGSERVERSIGNOUTDATA_PERFDATA._serialized_end=7194
  _CMSGSERVERSIGNOUTDATA_BOOKREWARDS._serialized_start=7197
  _CMSGSERVERSIGNOUTDATA_BOOKREWARDS._serialized_end=7464
  _CMSGSERVERSIGNOUTDATA_BOOKREWARDS_BOOKREWARD._serialized_start=7310
  _CMSGSERVERSIGNOUTDATA_BOOKREWARDS_BOOKREWARD._serialized_end=7358
  _CMSGSERVERSIGNOUTDATA_BOOKREWARDS_ACCOUNTREWARDS._serialized_start=7360
  _CMSGSERVERSIGNOUTDATA_BOOKREWARDS_ACCOUNTREWARDS._serialized_end=7464
  _CMSGSERVERSIGNOUTDATA_ACCOUNTSTATCHANGES._serialized_start=7467
  _CMSGSERVERSIGNOUTDATA_ACCOUNTSTATCHANGES._serialized_end=7795
  _CMSGSERVERSIGNOUTDATA_ACCOUNTSTATCHANGES_STAT._serialized_start=7590
  _CMSGSERVERSIGNOUTDATA_ACCOUNTSTATCHANGES_STAT._serialized_end=7696
  _CMSGSERVERSIGNOUTDATA_ACCOUNTSTATCHANGES_ACCOUNTSTATS._serialized_start=7698
  _CMSGSERVERSIGNOUTDATA_ACCOUNTSTATCHANGES_ACCOUNTSTATS._serialized_end=7795
  _CMSGSERVERSIGNOUTDATA_PLAYERCHAT._serialized_start=7798
  _CMSGSERVERSIGNOUTDATA_PLAYERCHAT._serialized_end=7986
  _CMSGSERVERSIGNOUTDATA_PLAYERCHAT_CHATLINE._serialized_start=7898
  _CMSGSERVERSIGNOUTDATA_PLAYERCHAT_CHATLINE._serialized_end=7986
  _CMSGSERVERSIGNOUTDATA_PENALIZEDPLAYERS._serialized_start=7989
  _CMSGSERVERSIGNOUTDATA_PENALIZEDPLAYERS._serialized_end=8393
  _CMSGSERVERSIGNOUTDATA_PENALIZEDPLAYERS_PENALTY._serialized_start=8108
  _CMSGSERVERSIGNOUTDATA_PENALIZEDPLAYERS_PENALTY._serialized_end=8277
  _CMSGSERVERSIGNOUTDATA_PENALIZEDPLAYERS_EPENALTYREASON._serialized_start=8279
  _CMSGSERVERSIGNOUTDATA_PENALIZEDPLAYERS_EPENALTYREASON._serialized_end=8393
  _CMSGMATCHDATA._serialized_start=8396
  _CMSGMATCHDATA._serialized_end=10451
  _CMSGMATCHDATA_PLAYERITEM._serialized_start=9014
  _CMSGMATCHDATA_PLAYERITEM._serialized_end=9147
  _CMSGMATCHDATA_PLAYERINFO._serialized_start=9150
  _CMSGMATCHDATA_PLAYERINFO._serialized_end=10278
  _CMSGMATCHDATA_EENDREASON._serialized_start=10281
  _CMSGMATCHDATA_EENDREASON._serialized_end=10451
  _CMSGSERVERTOGCMATCHSIGNOUT._serialized_start=10454
  _CMSGSERVERTOGCMATCHSIGNOUT._serialized_end=10641
  _CMSGSERVERTOGCMATCHSIGNOUTRESPONSE._serialized_start=10644
  _CMSGSERVERTOGCMATCHSIGNOUTRESPONSE._serialized_end=10949
  _CMSGSERVERTOGCMATCHSIGNOUTRESPONSE_ESIGNOUTRESULT._serialized_start=10776
  _CMSGSERVERTOGCMATCHSIGNOUTRESPONSE_ESIGNOUTRESULT._serialized_end=10949
  _CMSGSERVERWELCOMECITADEL._serialized_start=10951
  _CMSGSERVERWELCOMECITADEL._serialized_end=10977
  _CMSGSERVERTOGCIDLEPING._serialized_start=10979
  _CMSGSERVERTOGCIDLEPING._serialized_end=11027
  _CMSGGCTOSERVERREQUESTPING._serialized_start=11029
  _CMSGGCTOSERVERREQUESTPING._serialized_end=11056
  _CMSGGCTOSERVERALLOCATEFORMATCH._serialized_start=11058
  _CMSGGCTOSERVERALLOCATEFORMATCH._serialized_end=11108
  _CMSGGCTOSERVERALLOCATEFORMATCHRESPONSE._serialized_start=11110
  _CMSGGCTOSERVERALLOCATEFORMATCHRESPONSE._serialized_end=11167
  _CMSGSERVERTOGCENTERMATCHMAKING._serialized_start=11170
  _CMSGSERVERTOGCENTERMATCHMAKING._serialized_end=11380
  _CMSGGCTOSERVERCANCELALLOCATEFORMATCH._serialized_start=11382
  _CMSGGCTOSERVERCANCELALLOCATEFORMATCH._serialized_end=11438
  _CMSGSERVERTOGCUPDATELOBBYSERVERSTATE._serialized_start=11441
  _CMSGSERVERTOGCUPDATELOBBYSERVERSTATE._serialized_end=11592
  _CMSGSERVERTOGCABANDONMATCH._serialized_start=11595
  _CMSGSERVERTOGCABANDONMATCH._serialized_end=12296
  _CMSGSERVERTOGCABANDONMATCH_PLAYER._serialized_start=12154
  _CMSGSERVERTOGCABANDONMATCH_PLAYER._serialized_end=12224
  _CMSGSERVERTOGCABANDONMATCH_EREASON._serialized_start=12226
  _CMSGSERVERTOGCABANDONMATCH_EREASON._serialized_end=12296
  _CMSGSERVERTOGCABANDONMATCHRESPONSE._serialized_start=12298
  _CMSGSERVERTOGCABANDONMATCHRESPONSE._serialized_end=12334
  _CMSGSERVERTOGCTESTCONNECTION._serialized_start=12336
  _CMSGSERVERTOGCTESTCONNECTION._serialized_end=12366
  _CMSGSERVERTOGCTESTCONNECTIONRESPONSE._serialized_start=12368
  _CMSGSERVERTOGCTESTCONNECTIONRESPONSE._serialized_end=12439
  _CMSGGCTOSERVERSETSERVERCONVAR._serialized_start=12441
  _CMSGGCTOSERVERSETSERVERCONVAR._serialized_end=12515
  _CMSGGCTOSERVERSETSERVERCONVARRESPONSE._serialized_start=12517
  _CMSGGCTOSERVERSETSERVERCONVARRESPONSE._serialized_end=12573
  _CMSGGCTOSERVERADDSPECTATOR._serialized_start=12575
  _CMSGGCTOSERVERADDSPECTATOR._serialized_end=12670
  _CMSGGCTOSERVERADDSPECTATORRESPONSE._serialized_start=12673
  _CMSGGCTOSERVERADDSPECTATORRESPONSE._serialized_end=12891
  _CMSGGCTOSERVERADDSPECTATORRESPONSE_ERESPONSE._serialized_start=12823
  _CMSGGCTOSERVERADDSPECTATORRESPONSE_ERESPONSE._serialized_end=12891
  _CMSGSERVERTOGCREPORTCHEATER._serialized_start=12894
  _CMSGSERVERTOGCREPORTCHEATER._serialized_end=13044
  _CMSGSERVERTOGCREPORTCHEATERRESPONSE._serialized_start=13046
  _CMSGSERVERTOGCREPORTCHEATERRESPONSE._serialized_end=13100
# @@protoc_insertion_point(module_scope)
