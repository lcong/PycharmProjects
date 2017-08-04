rm=/bin/rm -f
CC= gcc
PROGNAME= temp
INCLUDES=  -I./ -I../Applications/MCU/


DEFINES= $(INCLUDES) $(DEFS) 
CFLAGS= -g -Os -Wall $(DEFINES)

SRCS = rsi_api_sysinit.c rsi_hal_mcu_interrupt.c rsi_hal_mcu_ioports.c rsi_hal_mcu_spi.c rsi_hal_mcu_timers.c rsi_interrupt.c rsi_lib_util.c rsi_spi_api.c rsi_spi_band.c rsi_spi_bootloader.c rsi_spi_disconnect.c rsi_spi_execute_cmd.c rsi_spi_framerdwr.c rsi_spi_functs.c rsi_spi_fwupgrade.c rsi_spi_iface_init.c rsi_spi_init.c rsi_spi_interrupt_handler.c rsi_spi_join.c rsi_spi_memrdwr.c rsi_spi_power_mode.c rsi_spi_query_bssid_nwtype.c rsi_spi_query_conn_status.c rsi_spi_query_fwversion.c rsi_spi_query_macaddress.c rsi_spi_read_packet.c rsi_spi_regrdwr.c rsi_spi_scan.c rsi_spi_send_raw_data.c rsi_spi_mode_select.c rsi_spi_store_config.c rsi_spi_query_rssi.c rsi_spi_feat_select.c rsi_spi_set_mac_addr.c

OBJS = rsi_api_sysinit.o rsi_hal_mcu_interrupt.o rsi_hal_mcu_ioports.o rsi_hal_mcu_spi.o rsi_hal_mcu_timers.o rsi_interrupt.o rsi_lib_util.o rsi_spi_api.o rsi_spi_band.o rsi_spi_bootloader.o rsi_spi_disconnect.o rsi_spi_execute_cmd.o rsi_spi_framerdwr.o rsi_spi_functs.o rsi_spi_fwupgrade.o rsi_spi_iface_init.o rsi_spi_init.o rsi_spi_interrupt_handler.o rsi_spi_join.o rsi_spi_memrdwr.o rsi_spi_power_mode.o rsi_spi_query_bssid_nwtype.o rsi_spi_query_conn_status.o rsi_spi_query_fwversion.o rsi_spi_query_macaddress.o rsi_spi_read_packet.o rsi_spi_regrdwr.o rsi_spi_scan.o rsi_spi_send_raw_data.o rsi_spi_mode_select.o rsi_spi_store_config.o rsi_spi_query_rssi.o rsi_spi_feat_select.o rsi_spi_set_mac_addr.o

.c.o:
	$(rm) $@
	$(CC) $(CFLAGS) -c $*.c

all: $(OBJS)

clean:
	$(rm) $(OBJS) *~
