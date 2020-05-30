--
-- Estructura de tabla para la tabla `ActiveProcess`
--

CREATE TABLE `ActiveProcess` (
  `IP` varchar(99) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Process` varchar(99) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ActiveUsers`
--

CREATE TABLE `ActiveUsers` (
  `IP` varchar(99) COLLATE utf8_unicode_ci NOT NULL,
  `User` varchar(99) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `InfoServer`
--

CREATE TABLE `InfoServer` (
  `IP` varchar(99) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ProcessorInfo` varchar(99) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ProcessorType` varchar(99) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `SOInfo`
--

CREATE TABLE `SOInfo` (
  `IP` varchar(99) COLLATE utf8_unicode_ci NOT NULL,
  `SOName` varchar(99) COLLATE utf8_unicode_ci NOT NULL,
  `SOVersion` varchar(99) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


