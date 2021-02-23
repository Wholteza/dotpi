from pathlib import Path
from dotpi.configuration_bootstrapper.enums.configuration_bootstrap_strategy import ConfigurationBootstrapStrategy
from dotpi.exceptions.strategy_not_found_error import StrategyNotFoundError
from dotpi.configuration_bootstrapper.strategies.ensure_file_contains_section_strategy import bootstrap as file_contains_sections_strategy


strategies = {
    ConfigurationBootstrapStrategy.ENSURE_FILE_CONTAINS_SECTIONS: file_contains_sections_strategy
}


def bootstrap(file_to_bootstrap_into: Path, file_with_bootstrap_code: Path, strategy: ConfigurationBootstrapStrategy):
    if strategy not in strategies:
        raise StrategyNotFoundError(strategy)
    strategies[strategy](file_with_bootstrap_code, file_to_bootstrap_into)
