 # ORDER MATTERS 

########################################################################################################################
#############################                       support                                #############################
########################################################################################################################

from waterpip.scripts.support.raster import check_gdal_open , set_band_descriptions, \
    gdal_info, check_dimensions, raster_to_array, count_raster_values, array_to_raster, \
        retrieve_raster_crs, rasterize_shape, create_polygon_index_dict, create_values_specific_mask, \
            mask_raster, match_raster, build_vrt        

from waterpip.scripts.support.vector import file_to_records, geodataframe_to_shapefile, \
    retrieve_geodataframe_bbox, retrieve_shapefile_crs, shape_reprojection, create_bbox_shapefile, \
        delete_shapefile, copy_shapefile, check_add_wpid_to_shapefile, create_spatial_index, \
            check_for_overlap, overlap_among_features, union_and_drop, polygonize_cleanup, \
                raster_to_polygon, compare_raster_vector_crs, records_to_shapefile , \
                    add_matched_values_to_shapefile, polygon_area_drop, calc_lat_lon_polygon_area, \
                        fill_small_polygon_holes 

from waterpip.scripts.support.statistics import dict_to_dataframe, output_table, \
    latlon_dist, ceiling_divide, floor_minus, calc_dual_array_statistics, calc_single_array_numpy_statistic, \
        calc_multiple_array_numpy_statistic, mostcommonzaxis, calc_field_statistics, \
            multiple_raster_zonal_stats, equal_dimensions_zonal_stats, single_raster_zonal_stats, \
            raster_count_statistics,  generate_zonal_stats_column_and_function

########################################################################################################################
#############################                       structure                              #############################
########################################################################################################################

from waterpip.scripts.structure.wapor_structure import WaporStructure

########################################################################################################################
#############################                       retrieval                              #############################
########################################################################################################################

from waterpip.scripts.retrieval.wapor_land_cover_classification_codes import wapor_lcc,\
    dissagregate_categories, check_categories_exist_in_count_dict, \
        check_categories_exist_in_categories_dict

from waterpip.scripts.retrieval.wapor_api import WaporAPI

from waterpip.scripts.retrieval.wapor_retrieval import WaporRetrieval, printWaitBar, generate_retrieval_attempts_dict, \
    retrieve_api_result, deconstruct_wapor_time_code

########################################################################################################################
#############################                       analysis                               #############################
########################################################################################################################

from waterpip.scripts.analysis.wapor_analysis import WaporAnalysis

########################################################################################################################
#############################                       visualisation                          #############################
########################################################################################################################

# to come

########################################################################################################################
#############################                       reporting                              #############################
########################################################################################################################

# to come