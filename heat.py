# script to convert FLUKA energy deposition to heat
import argparse
import pandas as pd


def getFiles(input, cycles):
    '''in: name of input folder, out: dataframe with regions and
    energies as columns.'''
    start = r"1Region"
    end = r"Total (integrated over volume):"
    Energy = []
    Region = []
    data = []
    for i in range(1, cycles + 1):
        file = input + f'00{i}.out'
        try:
            lines = []
            with open(file, 'r') as f:
                appending = False
                for line in f:
                    if end in line:
                        break
                    if start in line:
                        appending = True
                    if appending is True:
                        lines.append(line.split())
                lines = lines[4:-1]  # works around whitespace/headers
            data.append(lines)
        except FileNotFoundError:
            print('File not found')

    for line in data:
        for row in line:
            # casts to float and replaces double notation
            erg = float(row[5].replace('D', 'E'))
            Energy.append(erg)
            Region.append(row[1])

    dict = {'Region': Region, 'Energy': Energy}
    df = pd.DataFrame(dict)
    return df


def getInfo(input, current=0.006, cycles=5, mod_vol=1000):
    '''uses erg2heat() to convert energy from dataframe to heat
    and prints to terminal all the values. returns none'''
    df = getFiles(input, cycles)
    # makes a list of all unique elements in 'Region'
    regions = df['Region'].unique().tolist()
    print(r'''
-----------------------------------------
REGION   :: Heat (W/cm3)   +/- Standard Deviation
-----------------------------------------''')
    for region in regions:
        values = df['Energy'].where(df['Region'] == region)
        mean = erg2heat(float(values.mean()), current)
        std = erg2heat(float(values.std()), current)
        print(f'{region:8} :: {mean:.4e} +/- {std:.4e}')
        if region in ['WATERCNT', 'METHCNT', 'HYDCNT']:
            mod_reg = region
            mod_heat = mean * mod_vol
            mod_std = std * mod_vol
    print(42*'-', '\nNo. of Regions: %i' % len(regions))
    print(f'''Moderator ({mod_reg}) = {mod_heat:.2e} +/- {mod_std:.2e} [W/cm3]
{42*'-'}''')


def erg2heat(val, current):
    '''energy dep * volume * 1.6E-10 [to convert to joules] *
    current / charge [equivalent to primaries (real) per time]
    == heat (watts)'''
    heat = val * 1E9 * current
    return heat


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
                                     script to convert FLUKA
                                     energy deposition to heat''')
    parser.add_argument('inp', type=str, help='name / path to .out files')
    parser.add_argument('current', nargs='?', default=0.006, type=float)
    parser.add_argument('cycles', nargs='?', default=5)
    parser.add_argument('vol', help='moderator volume, default=1000',
                        default=1000.0, type=float, nargs='?')

    args = parser.parse_args()
    getInfo(args.inp, args.current, args.cycles, args.vol)
