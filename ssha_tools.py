import arcpy
import random
import Working_RC_Calcs
import HHCalculations
import utils
import os

def write_peak_flows_to_sewers(study_areas, study_sewers):
	"""
	write the peak runoff stored in the study areas layer to each studied sewer
	"""

	fields = ['Project_ID', 'StudyArea_ID', 'Peak_Runoff']
	with arcpy.da.SearchCursor(study_areas, fields) as areas_cursor:
		for area in areas_cursor:
			project_id = area[0]
			study_area_id = area[1]
			peak_runoff = area[2]
			# arcpy.AddMessage('{} - {} peak runoff = {}'.format(project_id, study_area_id, peak_runoff))
			print '{} - {} peak runoff = {}'.format(project_id, study_area_id, peak_runoff)
			#update the peakflow in the study sewer
			ss_fields = ['Peak_Runoff']
			where = "Project_ID = {} AND StudyArea_ID = '{}' AND StudySewer = 'Y'".format(project_id, study_area_id)
			with arcpy.da.UpdateCursor(study_sewers, ss_fields, where_clause=where) as cursor:
				for sewer in cursor:
					sewer[0] = peak_runoff

					cursor.updateRow(sewer)


def updateDAIndex (project_id, study_areas, study_area_indices):

	"""
	update the companion "Drainage Area Index" for the current project id. This
	essentially copies the drainage areas with the project id and creates a new
	feature class. This compainion feature class is used for Data Driven Pages
	functionality.
	"""

	#check if index already exists, delete if necessary
	index_layer = os.path.join(study_area_indices, "DA_" + project_id)
	if arcpy.Exists(index_layer):
		arcpy.AddMessage('{} index exists, overwriting...'.format(project_id))
		arcpy.Delete_management(index_layer)

	where = "Project_ID = " + project_id
	layer_name = "DA_" + project_id

	arcpy.MakeFeatureLayer_management(study_areas, index_layer, where_clause = where)
	arcpy.FeatureClassToFeatureClass_conversion(index_layer, study_area_indices, layer_name)
	arcpy.Delete_management(index_layer)
