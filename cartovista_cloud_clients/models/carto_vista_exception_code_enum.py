# coding: utf-8

"""
    CartoVista REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CartoVistaExceptionCodeEnum(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    UNKNOWN = "Unknown"
    OK = "OK"
    EXPIREDCLAIMSSTRUCTURE = "ExpiredClaimsStructure"
    INVALIDWEBSERVICEREQUEST = "InvalidWebServiceRequest"
    UNAUTHORIZED = "Unauthorized"
    FORBIDDEN = "Forbidden"
    ERROR = "Error"
    NOTFOUND = "NotFound"
    INVALIDFOLDERNAME = "InvalidFolderName"
    SYSTEMFOLDERNOTDELETABLE = "SystemFolderNotDeletable"
    FOLDERNOTEMPTY = "FolderNotEmpty"
    INVALIDUPLOADFORMAT = "InvalidUploadFormat"
    REDISERROR = "RedisError"
    REDISUNAVAILABLE = "RedisUnavailable"
    INVALIDFOLDER = "InvalidFolder"
    USERCREATEFAILED = "UserCreateFailed"
    USERUPDATEFAILED = "UserUpdateFailed"
    USERNAMEOREMAILALREADYEXISTS = "UsernameOrEmailAlreadyExists"
    USERUPDATENOTALLOWED = "UserUpdateNotAllowed"
    INVALIDEMAILADDRESS = "InvalidEmailAddress"
    GROUPCREATEFAILED = "GroupCreateFailed"
    GROUPUPDATEFAILED = "GroupUpdateFailed"
    GROUPNAMEALREADYEXISTS = "GroupNameAlreadyExists"
    GROUPNAMETOOLONG = "GroupNameTooLong"
    USERSNOTIMPORTABLE = "UsersNotImportable"
    GROUPSNOTIMPORTABLE = "GroupsNotImportable"
    INVALIDPROVIDER = "InvalidProvider"
    INVALIDEMAILDOMAIN = "InvalidEmailDomain"
    CANTCHANGEUSERSINACTIVEDIRECTORYGROUP = "CantChangeUsersInActiveDirectoryGroup"
    CANTREMOVELASTADMINISTRATOR = "CantRemoveLastAdministrator"
    NOTWHITELISTED = "NotWhitelisted"
    TENANTCREATEFAILED = "TenantCreateFailed"
    TENANTUPDATEFAILED = "TenantUpdateFailed"
    TENANTNAMEALREADYEXISTS = "TenantNameAlreadyExists"
    TENANTURLCODEINUSE = "TenantURLCodeInUse"
    TENANTISDELETED = "TenantIsDeleted"
    TENANTISLASTACTIVE = "TenantIsLastActive"
    TENANTDISCLAIMERCREATEFAILED = "TenantDisclaimerCreateFailed"
    TENANTDISCLAIMERUPDATEFAILED = "TenantDisclaimerUpdateFailed"
    TENANTDISCLAIMERGETFAILED = "TenantDisclaimerGetFailed"
    TENANTDISCLAIMERALREADYEXISTS = "TenantDisclaimerAlreadyExists"
    TENANTEMAILCREATEFAILED = "TenantEmailCreateFailed"
    TENANTEMAILUPDATEFAILED = "TenantEmailUpdateFailed"
    TENANTEMAILGETFAILED = "TenantEmailGetFailed"
    TENANTEMAILALREADYEXISTS = "TenantEmailAlreadyExists"
    TENANTSTORAGELIMITREACHED = "TenantStorageLimitReached"
    COMPANYNAMEEXISTSORISINVALID = "CompanyNameExistsOrIsInvalid"
    NOPERMISSIONS = "NoPermissions"
    LOGINFAILED = "LoginFailed"
    INACTIVETENANT = "InactiveTenant"
    INVALIDTENANTLICENSE = "InvalidTenantLicense"
    INVALIDTENANTSUBSCRIPTION = "InvalidTenantSubscription"
    INVALIDUSERNAMEORPASSWORD = "InvalidUserNameOrPassword"
    THEREISNOTENANTDEFINEDWITHNAME = "ThereIsNoTenantDefinedWithName"
    INVALIDRECAPTCHA = "InvalidReCaptcha"
    ACCOUNTISLOCKOUT = "AccountIsLockout"
    BLOCKEDIPADDRESS = "BlockedIpAddress"
    IPADDRESSNOTWHITELISTED = "IpAddressNotWhitelisted"
    INVALIDEXTERNALPROVIDERTOKEN = "InvalidExternalProviderToken"
    INVALIDLICENSE = "InvalidLicense"
    LICENSEEXPIRED = "LicenseExpired"
    NOTVALIDATED = "NotValidated"
    INVALIDSERIALCODE = "InvalidSerialCode"
    INVALIDSIGNATURE = "InvalidSignature"
    INVALIDMACHINECODE = "InvalidMachineCode"
    INVALIDUSAGEMODE = "InvalidUsageMode"
    ACTIVATIONFAILED = "ActivationFailed"
    DEACTIVATED = "Deactivated"
    INVALIDDOMAIN = "InvalidDomain"
    MAXNUMUSERS = "MaxNumUsers"
    FEATURELOCKED = "FeatureLocked"
    DATAUPLOADFAILED = "DataUploadFailed"
    NOTZIPFILE = "NotZipFile"
    NOSUPPORTEDFORMATINZIP = "NoSupportedFormatInZip"
    TOOMANYSUPPORTEDFORMATINZIP = "TooManySupportedFormatInZip"
    INVALIDZIPCONTENT = "invalidZipContent"
    INVALIDZIPCONTENTMISSINGINDEXHTML = "invalidZipContentMissingIndexHTML"
    MAPINFOEXTENDEDNOTSUPPORTED = "MapInfoExtendedNotSupported"
    MAPVERSIONNOTSUPPORTED = "MapVersionNotSupported"
    SETUNIQUECOLUMN = "SetUniqueColumn"
    COLUMNNOTUNIQUE = "ColumnNotUnique"
    GEOMETRYTYPENOTFOUND = "GeometryTypeNotFound"
    TOOLARGENUMBER = "TooLargeNumber"
    DUPLICATECOLUMNNAME = "DuplicateColumnName"
    NOSHEETS = "NoSheets"
    APPEND = "Append"
    DATAINUSE = "DataInUse"
    MUSTBETILED = "MustBeTiled"
    COLUMNCANTHAVEDUPLICATES = "ColumnCantHaveDuplicates"
    COLUMNTYPESMISMATCH = "ColumnTypesMismatch"
    COLUMNIDANDROWCOUNTNOTEQUAL = "ColumnIdAndRowCountNotEqual"
    CANTSETVALUEFORINTERNALCOLUMN = "CantSetValueForInternalColumn"
    COLUMNNOTINDATATABLE = "ColumnNotInDataTable"
    CANTSETDATETIMEASUNIQUECOLUMN = "CantSetDateTimeAsUniqueColumn"
    GETDATAROWERROR = "GetDataRowError"
    CANTDELETEUNIQUECOLUMN = "CantDeleteUniqueColumn"
    CANTCONVERTBETWEENDATETIMEANDNUMERIC = "CantConvertBetweenDateTimeAndNumeric"
    UPDATETYPEINVALIDDATA = "UpdateTypeInvalidData"
    UPDATETYPEINVALIDDATE = "UpdateTypeInvalidDate"
    INVALIDAGGREGATIONTYPE = "InvalidAggregationType"
    INVALIDDATAJOIN = "InvalidDataJoin"
    DATAJOINTARGETMUSTBEALAYER = "DataJoinTargetMustBeALayer"
    DATAJOINSOURCECANNOTBEALAYER = "DataJoinSourceCannotBeALayer"
    ONETOONEJOINHASMORELINKSTHANRECORDS = "OneToOneJoinHasMoreLinksThanRecords"
    INVALIDTIMESERIES = "InvalidTimeSeries"
    TIMESERIESCOLUMNMUSTBENUMBERORDATE = "TimeSeriesColumnMustBeNumberOrDate"
    TIMESERIESCOLUMNCANNOTBENULLWHENONETOMANYJOINSEXIST = "TimeSeriesColumnCannotBeNullWhenOneToManyJoinsExist"
    COLUMNUSEDINTIMESERIES = "ColumnUsedInTimeSeries"
    GEOCODINGLIMITEXCEEDED = "GeocodingLimitExceeded"
    CANTDELETESOURCELAYER = "CantDeleteSourceLayer"
    CANTEDITDEMOLAYERDATA = "CantEditDemoLayerData"
    CANTMODIFYLAYERSOURCESTRUCTURE = "CantModifyLayerSourceStructure"
    INVALIDHEATMAPPARAMETERS = "InvalidHeatmapParameters"
    INVALIDHEATMAPRESOLUTION = "InvalidHeatmapResolution"
    HEATMAPALREADYGENERATED = "HeatmapAlreadyGenerated"
    HEATMAPSOURCECANNOTBECHANGED = "HeatmapSourceCannotBeChanged"
    HEATMAPISGENERATING = "HeatmapIsGenerating"
    INVALIDLATLONGDATA = "InvalidLatLongData"
    UNRECOGNIZEDPROJ4STRING = "UnrecognizedProj4String"
    MAPUPLOADERROR = "MapUploadError"
    MAPINUSE = "MapInUse"
    MAPHASNONONTILEDSERVERLAYER = "MapHasNoNonTiledServerLayer"
    MAPMUSTBEDYNAMIC = "MapMustBeDynamic"
    LAYERFORMAPNOTFOUND = "LayerForMapNotFound"
    MAPTOTERRITORYCONVERSIONCONFLICT = "MapToTerritoryConversionConflict"
    MAPTOTERRITORYCONVERSIONSETTINGSREQUIRED = "MapToTerritoryConversionSettingsRequired"
    TERRITORYSTATUSUPDATENOTALLOWED = "TerritoryStatusUpdateNotAllowed"
    TERRITORYMANAGERSETTINGSUPDATEFAILED = "TerritoryManagerSettingsUpdateFailed"
    TERRITORYMANAGERSETTINGSNULLVALUESINURBANICITYCOLUMN = "TerritoryManagerSettingsNullValuesInUrbanicityColumn"
    TERRITORYMANAGERSETTINGSNOZONES = "TerritoryManagerSettingsNoZones"
    TERRITORYMANAGERSETTINGSONLYONEIMPLANTATIONANDPTA = "TerritoryManagerSettingsOnlyOneImplantationAndPTA"
    TERRITORYMANAGERSETTINGSIMPLANTATIONANDPTACANNOTBEDELETED = "TerritoryManagerSettingsImplantationAndPTACannotBeDeleted"
    TERRITORYMANAGERSETTINGSINVALIDZONE = "TerritoryManagerSettingsInvalidZone"
    TERRITORYMANAGERSETTINGSZONESNOTORDERED = "TerritoryManagerSettingsZonesNotOrdered"
    INVALIDTERRITORYPARAMETERS = "InvalidTerritoryParameters"
    ALLANDONLYTHEUSERDEFINEDZONESMUSTBEPRESENT = "AllAndOnlyTheUserDefinedZonesMustBePresent"
    AZEROVALUESHOULDBEFOLLOWEDBYZERO = "AZeroValueShouldBeFollowedByZero"
    VALUESMUSTBEORDERED = "ValuesMustBeOrdered"
    ONLYZONEVALUESUPDATEALLOWED = "OnlyZoneValuesUpdateAllowed"
    UNRECOGNIZEDTERRITORYMANAGERZONE = "UnrecognizedTerritoryManagerZone"
    INVALIDISOCHRONERANGE = "InvalidIsochroneRange"
    INVALIDISOCHRONETRANSPORTTYPE = "InvalidIsochroneTransportType"
    COLUMNNOTINBLOCKLAYER = "ColumnNotInBlockLayer"
    TOOMANYVALUES = "TooManyValues"
    SESSIONUNAVAILABLE = "SessionUnavailable"
    TERRITORYMANAGEMENTLAYERUNIQUEIDNOTSET = "TerritoryManagementLayerUniqueIdNotSet"
    TERRITORYMANAGEMENTLAYERCANONLYBEUSEDONCE = "TerritoryManagementLayerCanOnlyBeUsedOnce"
    INVALIDTERRITORYNAMECOLUMN = "InvalidTerritoryNameColumn"
    INVALIDZONEDRIVETIME = "InvalidZoneDriveTime"
    INVALIDTERRITORYEXCLUSIVITYZONE = "InvalidTerritoryExclusivityZone"
    INVALIDTERRITORYPTAZONE = "InvalidTerritoryPtaZone"
    INVALIDTERRITORYBLOCKCONFLICTSRESOLUTION = "InvalidTerritoryBlockConflictsResolution"
    INVALIDTERRITORYBLOCKUPDATE = "InvalidTerritoryBlockUpdate"
    INVALIDZONEDELETEACTION = "InvalidZoneDeleteAction"
    INVALIDNUMBEROFZONES = "InvalidNumberOfZones"
    INVALIDTERRITORYLOCATION = "InvalidTerritoryLocation"
    SESSIONUPDATEFAILED = "SessionUpdateFailed"
    SESSIONCREATEFAILED = "SessionCreateFailed"
    SESSIONUNIQUECOLUMNCHANGED = "SessionUniqueColumnChanged"
    CANTDELETELASTSLIDE = "CantDeleteLastSlide"
    DATAQUERYMAXCOUNTEXCEEDED = "DataQueryMaxCountExceeded"
    IDENTIFIERALREADYINUSE = "IdentifierAlreadyInUse"
    IDENTIFIERCANNOTBENULL = "IdentifierCannotBeNull"
    NAMEALREADYINUSE = "NameAlreadyInUse"
    IDENTIFIERCONTAINSINVALIDCHARACTER = "IdentifierContainsInvalidCharacter"
    IDENTIFIERTOOLONG = "IdentifierTooLong"
    NAMETOOLONG = "NameTooLong"
    OBSERVATORYCREATEFAILED = "ObservatoryCreateFailed"
    OBSERVATORYUPDATEFAILED = "ObservatoryUpdateFailed"
    URLALREADYEXISTS = "UrlAlreadyExists"
    LINKREPRESENTATIONSFAILED = "LinkRepresentationsFailed"
    UNLINKREPRESENTATIONSFAILED = "UnlinkRepresentationsFailed"
    REPRESENTATIONMAPSNOTMATCHING = "RepresentationMapsNotMatching"
    REPRESENTATIONNOTFOUND = "RepresentationNotFound"
    DIMENSIONCREATEFAILED = "DimensionCreateFailed"
    ONLYONESPATIALDIMENSIONALLOWED = "OnlyOneSpatialDimensionAllowed"
    MISSINGREQUIREDDIMENSIONS = "MissingRequiredDimensions"
    INVALIDDATACOLUMN = "InvalidDataColumn"
    DATACOLUMNALREADYINUSE = "DataColumnAlreadyInUse"
    DIMENSIONUPDATEFAILED = "DimensionUpdateFailed"
    SPATIALDIMENSIONCANNOTBEOPTIONAL = "SpatialDimensionCannotBeOptional"
    CREATEIMAGELIBRARYFAILED = "CreateImageLibraryFailed"
    DELETEIMAGELIBRARYFAILED = "DeleteImageLibraryFailed"
    GETIMAGELIBRARYFAILED = "GetImageLibraryFailed"
    UPDATEIMAGELIBRARYFAILED = "UpdateImageLibraryFailed"
    INVALIDGEOMETRYTYPE = "InvalidGeometryType"
    ROWCOUNTOUTSIDEOFRANGE = "RowCountOutsideOfRange"
    COLUMNUSEDINJOIN = "ColumnUsedInJoin"
    CREATEUPDATEFAILED = "CreateUpdateFailed"
    UNIQUECOLUMNREQUIRED = "UniqueColumnRequired"
    UNIQUECOLUMNMISSINGINLIST = "UniqueColumnMissingInList"
    DELETEFAILED = "DeleteFailed"
    EXTERNALLAYER = "ExternalLayer"
    INVALIDEXTERNALLAYERURL = "InvalidExternalLayerUrl"
    GRIDLAYERUPLOADFAILED = "GridLayerUploadFailed"
    PROJECTIONNOTFOUND = "ProjectionNotFound"
    CANTDELETELASTGRIDSOURCE = "CantDeleteLastGridSource"
    INVALIDGRIDLAYERREQUESTHEADERRANGE = "InvalidGridLayerRequestHeaderRange"
    CANNOTADDRGBTONUMERICGRIDLAYER = "CannotAddRGBToNumericGridLayer"
    CANNOTADDNUMERICTORGBGRIDLAYER = "CannotAddNumericToRGBGridLayer"
    SELECTIONTOOLARGE = "SelectionTooLarge"
    SELECTIONHASNOINTERSECTION = "SelectionHasNoIntersection"
    INVALIDINTERSECTION = "InvalidIntersection"
    VIEWCREATIONERROR = "ViewCreationError"
    COLUMNTYPENOTALLOWED = "ColumnTypeNotAllowed"
    VIEWEXPRESSIONCANNOTHAVEACOLUMN = "ViewExpressionCannotHaveAColumn"
    VIEWFROMCOLUMNMUSTHAVEACOLUMN = "ViewFromColumnMustHaveAColumn"
    VIEWUPDATEERROR = "ViewUpdateError"
    ONLYREADPERMISSIONONVIEWS = "OnlyReadPermissionOnViews"
    INVALIDVIEWEXPRESSION = "InvalidViewExpression"
    VIEWSMUSTDELETEDBEFORECREATINGNEWONES = "ViewsMustDeletedBeforeCreatingNewOnes"
    WEIGHTOUTOFBOUND = "WeightOutOfBound"
    VARIABLEUPDATEERROR = "VariableUpdateError"
    UPDATEVARIABLEFORBIDDEN = "UpdateVariableForbidden"
    CANNOTOPTIMIZENONTILEDLAYER = "CannotOptimizeNonTiledLayer"
    MAXIMUMMAPS = "MaximumMaps"
    MAXIMUMLAYERSPERMAP = "MaximumLayersPerMap"
    MAPLOCKED = "MapLocked"
    INVALIDSYMBOL = "InvalidSymbol"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """CartoVistaExceptionCodeEnum - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CartoVistaExceptionCodeEnum, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CartoVistaExceptionCodeEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
